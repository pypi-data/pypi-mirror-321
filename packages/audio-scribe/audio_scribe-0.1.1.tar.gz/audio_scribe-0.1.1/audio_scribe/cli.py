#!/usr/bin/env python3
"""
Audio Scribe 
-----------------
A command-line script for transcribing audio files with speaker diarization
using Whisper and Pyannote. The script uses a Hugging Face token for
downloading Pyannote speaker-diarization models and displays a progress bar
with resource usage while transcribing.
"""

print("Initializing environment... Please wait while we load dependencies and models.")
import sys
sys.stdout.flush()

import os
import glob
import wave
import json
import logging
import warnings
import argparse
import readline
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict
from dataclasses import dataclass
import base64

# Core dependencies
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import torch
import whisper
import importlib.metadata
from importlib.metadata import PackageNotFoundError
from pyannote.audio import Pipeline

# Progress bar dependencies - imported via HAVE_PROGRESS_SUPPORT from __init__
try:
    from alive_progress import alive_bar
    import psutil
    import GPUtil
    HAVE_PROGRESS_SUPPORT = True
except ImportError:
    HAVE_PROGRESS_SUPPORT = False


# Configure logging
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("transcription.log", mode="a", encoding="utf-8"),
    ],
)
logger = logging.getLogger(__name__)

# ---------- FILE PATH TAB-COMPLETION SNIPPET ----------
def complete_path(text, state):
    """
    Return the 'state'-th completion for 'text'.
    This function will be used by 'readline' to enable file path autocompletion.
    """
    # If the user typed a glob pattern (with * or ?)
    if '*' in text or '?' in text:
        matches = glob.glob(text)
    else:
        # Split off the directory name and partial file/directory name
        directory, partial = os.path.split(text)
        if not directory:
            directory = '.'
        try:
            # List everything in 'directory' that starts with 'partial'
            entries = os.listdir(directory)
        except OSError:
            # If directory doesn't exist or we lack permission, no matches
            entries = []

        matches = []
        for entry in entries:
            if entry.startswith(partial):
                full_path = os.path.join(directory, entry)
                # If it's a directory, add a trailing slash to indicate that
                if os.path.isdir(full_path) and not full_path.endswith(os.path.sep):
                    full_path += os.path.sep
                matches.append(full_path)

    # Sort matches to have a consistent order
    matches.sort()

    # If 'state' is beyond last match, return None
    return matches[state] if state < len(matches) else None


@dataclass
class TranscriptionConfig:
    """
    Configuration settings for the transcription pipeline.
    """
    output_directory: Path
    whisper_model: str = "base.en"
    diarization_model: str = "pyannote/speaker-diarization-3.1"
    temp_directory: Optional[Path] = None
    device: Optional[str] = None

    def __post_init__(self):
        # Use CUDA if available, else fall back to CPU
        self.device = self.device or ("cuda" if torch.cuda.is_available() else "cpu")
        # Default temp directory inside the output directory
        self.temp_directory = self.temp_directory or (self.output_directory / "temp")
        # Ensure directories exist
        self.temp_directory.mkdir(parents=True, exist_ok=True)
        self.output_directory.mkdir(parents=True, exist_ok=True)


class TokenManager:
    """
    Handles secure storage and retrieval of the Hugging Face authentication token.
    """
    def __init__(self):
        # Store config in ~/.pyannote/config.json
        self.config_dir = Path.home() / ".pyannote"
        self.config_file = self.config_dir / "config.json"
        self._initialize_config()

    def _initialize_config(self) -> None:
        """
        Initialize configuration directory and file with secure permissions.
        """
        self.config_dir.mkdir(exist_ok=True)
        if not self.config_file.exists():
            self._save_config({})

        # Set secure file and directory permissions on POSIX systems
        if os.name == "posix":
            os.chmod(self.config_dir, 0o700)
            os.chmod(self.config_file, 0o600)

    def _get_encryption_key(self) -> bytes:
        """
        Generate an encryption key from system-specific data.
        """
        salt = b"pyannote-audio-salt"
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = kdf.derive(str(Path.home()).encode())
        return base64.urlsafe_b64encode(key)

    def _save_config(self, config: dict) -> None:
        """
        Securely save configuration to file.
        """
        with open(self.config_file, "w", encoding="utf-8") as f:
            json.dump(config, f)

    def _load_config(self) -> dict:
        """
        Load configuration from file.
        """
        try:
            with open(self.config_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    def store_token(self, token: str) -> bool:
        """
        Securely store authentication token.
        """
        try:
            fernet = Fernet(self._get_encryption_key())
            encrypted_token = fernet.encrypt(token.encode())

            config = self._load_config()
            config["token"] = encrypted_token.decode()

            self._save_config(config)
            return True
        except Exception as e:
            logger.error(f"Failed to store token: {e}")
            return False

    def retrieve_token(self) -> Optional[str]:
        """
        Retrieve stored authentication token.
        """
        try:
            config = self._load_config()
            if "token" in config:
                fernet = Fernet(self._get_encryption_key())
                return fernet.decrypt(config["token"].encode()).decode()
        except Exception as e:
            logger.error(f"Failed to retrieve token: {e}")
        return None

    def delete_token(self) -> bool:
        """
        Delete stored authentication token.
        """
        try:
            config = self._load_config()
            if "token" in config:
                del config["token"]
                self._save_config(config)
            return True
        except Exception as e:
            logger.error(f"Failed to delete token: {e}")
            return False


class DependencyManager:
    """
    Manages and verifies system dependencies using importlib.metadata.
    """
    REQUIRED_PACKAGES = {
        "torch": None,
        "pyannote.audio": None,
        "openai-whisper": None,
        "pytorch-lightning": None,
        "keyring": None,
    }

    @classmethod
    def verify_dependencies(cls) -> bool:
        """
        Verify all required dependencies are installed with correct versions
        (if specified). Returns True if all are installed and correct, False otherwise.
        """
        missing = []
        outdated = []

        for package, required_version in cls.REQUIRED_PACKAGES.items():
            try:
                installed_version = importlib.metadata.version(package)
                if required_version and installed_version != required_version:
                    outdated.append(
                        f"{package} (installed: {installed_version}, required: {required_version})"
                    )
            except PackageNotFoundError:
                missing.append(package)

        if missing or outdated:
            if missing:
                logger.error("Missing packages: %s", ", ".join(missing))
            if outdated:
                logger.error("Outdated packages: %s", ", ".join(outdated))
            logger.info(
                "Install required packages: pip install %s",
                " ".join(
                    f"{pkg}=={ver}" if ver else pkg
                    for pkg, ver in cls.REQUIRED_PACKAGES.items()
                ),
            )
            return False
        return True


class AudioProcessor:
    """
    Handles audio file processing and segmentation using the `wave` module.
    """
    def __init__(self, config: TranscriptionConfig):
        self.config = config

    def load_audio_segment(
        self,
        audio_path: Path,
        start_time: float,
        end_time: float,
        output_path: Path,
    ) -> bool:
        """
        Extract and save the audio segment from `start_time` to `end_time`.
        """
        try:
            with wave.open(str(audio_path), "rb") as infile:
                params = infile.getparams()
                frame_rate = params.framerate
                start_frame = int(start_time * frame_rate)
                end_frame = min(int(end_time * frame_rate), infile.getnframes())

                infile.setpos(start_frame)
                frames = infile.readframes(end_frame - start_frame)

                with wave.open(str(output_path), "wb") as outfile:
                    outfile.setparams(params)
                    outfile.writeframes(frames)
            return True
        except Exception as e:
            logger.error(f"Failed to process audio segment: {e}")
            return False


class TranscriptionPipeline:
    """
    Main pipeline for audio transcription (Whisper) and speaker diarization (Pyannote).
    """
    def __init__(self, config: TranscriptionConfig):
        self.config = config
        self.diarization_pipeline = None
        self.whisper_model = None
        self.token_manager = TokenManager()
        self._running = False  # used for resource monitor thread

    def initialize_models(self, auth_token: str) -> bool:
        """
        Initialize the Pyannote diarization pipeline and the Whisper model.
        """
        try:
            # Load Whisper model (set download root to avoid clutter in home directory)
            self.whisper_model = whisper.load_model(
                self.config.whisper_model,
                device=self.config.device,
                download_root=str(self.config.output_directory / "models"),
            )

            # Load Pyannote diarization pipeline
            self.diarization_pipeline = Pipeline.from_pretrained(
                self.config.diarization_model, use_auth_token=auth_token
            )
            self.diarization_pipeline.to(torch.device(self.config.device))

            if self.config.device == "cpu":
                warnings.warn("Running on CPU. GPU is recommended for better performance.")

            return True
        except Exception as e:
            logger.error(f"Model initialization failed: {e}")
            logger.error("Please ensure you have accepted the model conditions at:")
            logger.error("  1. https://huggingface.co/pyannote/segmentation-3.0")
            logger.error("  2. https://huggingface.co/pyannote/speaker-diarization-3.1")
            return False

    def _update_resources(self, bar):
        """
        Continuously update progress bar text with CPU/MEM/GPU usage, until self._running is False.
        """
        while self._running:
            try:
                import time
                time.sleep(0.5)

                cpu_usage = psutil.cpu_percent(interval=None) if HAVE_PROGRESS_SUPPORT else 0
                memory_usage = psutil.virtual_memory().percent if HAVE_PROGRESS_SUPPORT else 0

                if HAVE_PROGRESS_SUPPORT and GPUtil.getGPUs():
                    gpus = GPUtil.getGPUs()
                    gpu_mem_used = f"{gpus[0].memoryUsed:.0f}"
                    gpu_mem_total = f"{gpus[0].memoryTotal:.0f}"
                    gpu_usage_text = f"{gpu_mem_used}/{gpu_mem_total} MB"
                else:
                    gpu_usage_text = "N/A"

                resource_text = f"CPU: {cpu_usage}%, MEM: {memory_usage}%, GPU Mem: {gpu_usage_text}"
                bar.text(resource_text)
            except Exception as e:
                logger.error(f"Resource monitoring error: {e}")

    def process_file(self, audio_path: Path) -> bool:
        """
        Diarize, segment, and transcribe using Whisper + Pyannote with progress feedback.
        """
        try:
            logger.info("Starting audio processing...")
            diarization = self.diarization_pipeline(str(audio_path))
            segments = list(diarization.itertracks(yield_label=True))
            total_segments = len(segments)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = self.config.output_directory / f"transcript_{timestamp}.txt"
            audio_processor = AudioProcessor(self.config)

            if not HAVE_PROGRESS_SUPPORT:
                # No alive_progress, psutil, or GPUtil installed
                logger.info("Processing audio without progress bar (missing optional packages).")
                with output_file.open("w", encoding="utf-8") as f:
                    for turn, _, speaker in segments:
                        segment_path = (
                            self.config.temp_directory
                            / f"segment_{speaker}_{turn.start:.2f}_{turn.end:.2f}.wav"
                        )
                        if self.audio_processor.load_audio_segment(audio_path, turn.start, turn.end, segment_path):
                            transcription = self.whisper_model.transcribe(str(segment_path))["text"]
                            segment_path.unlink(missing_ok=True)

                            line = f"[{turn.start:.2f}s - {turn.end:.2f}s] Speaker {speaker}: {transcription.strip()}\n"
                            f.write(line)
                            logger.info(line.strip())
                return True
            else:
                # Use a progress bar to track segment transcription
                from alive_progress import alive_bar
                import threading

                self._running = True
                with output_file.open("w", encoding="utf-8") as f, alive_bar(
                    total_segments,
                    title="Transcribing Audio",
                    spinner="pulse",
                    theme="classic",
                    stats=False,
                    elapsed=True,
                    monitor=True,
                ) as bar:

                    # Start a background thread for resource monitoring
                    resource_thread = threading.Thread(target=self._update_resources, args=(bar,))
                    resource_thread.start()

                    for turn, _, speaker in segments:
                        segment_path = (
                            self.config.temp_directory
                            / f"segment_{speaker}_{turn.start:.2f}_{turn.end:.2f}.wav"
                        )
                        if audio_processor.load_audio_segment(audio_path, turn.start, turn.end, segment_path):
                            transcription = self.whisper_model.transcribe(str(segment_path))["text"]
                            segment_path.unlink(missing_ok=True)

                            line = f"[{turn.start:.2f}s - {turn.end:.2f}s] Speaker {speaker}: {transcription.strip()}\n"
                            f.write(line)
                            logger.info(line.strip())

                        # Update the progress bar
                        bar()

                    # Stop resource monitoring
                    self._running = False
                    resource_thread.join()

            logger.info(f"Transcription completed. Output saved to: {output_file}")
            return True

        except Exception as e:
            logger.error(f"Processing failed: {e}")
            return False


def get_token(token_manager: TokenManager) -> Optional[str]:
    """
    Get authentication token from storage or user input.
    """
    stored_token = token_manager.retrieve_token()
    if stored_token:
        choice = input("\nUse the stored Hugging Face token? (y/n): ").lower().strip()
        if choice == "y":
            return stored_token

    print("\nA HuggingFace token is required for speaker diarization.")
    print("Get your token at: https://huggingface.co/settings/tokens")
    print("\nEnsure you have accepted:")
    print("  1. pyannote/segmentation-3.0 conditions")
    print("  2. pyannote/speaker-diarization-3.1 conditions")

    token = input("\nEnter HuggingFace token: ").strip()
    if token:
        choice = input("Save token for future use? (y/n): ").lower().strip()
        if choice == "y":
            if token_manager.store_token(token):
                print("Token saved successfully.")
            else:
                print("Failed to save token. It will be used for this session only.")
    return token if token else None


def main():
    parser = argparse.ArgumentParser(
        description="Audio Transcription Pipeline using Whisper + Pyannote, with optional progress bar."
    )
    parser.add_argument(
        "--audio", 
        type=Path, 
        help="Path to the audio file to transcribe."
    )
    parser.add_argument(
        "--token", 
        help="HuggingFace API token. Overrides any saved token."
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Path to the output directory for transcripts and temporary files.",
    )
    parser.add_argument(
        "--delete-token",
        action="store_true",
        help="Delete any stored Hugging Face token and exit.",
    )
    parser.add_argument(
        "--show-warnings",
        action="store_true",
        help="Enable user warnings (e.g., from pyannote.audio). Disabled by default.",
    )
    parser.add_argument(
        "--whisper-model",
        default="base.en",
        help="Specify the Whisper model to use (default: 'base.en').",
    )
    args = parser.parse_args()

    # Manage user warnings
    if not args.show_warnings:
        warnings.filterwarnings("ignore", category=UserWarning, module=r"pyannote\.audio")
        warnings.filterwarnings("ignore", category=FutureWarning, module="whisper")
    else:
        warnings.resetwarnings()

    # Check dependencies
    if not DependencyManager.verify_dependencies():
        sys.exit(1)

    # Initialize tab-completion for file paths (Unix-like only, or with pyreadline on Windows)
    readline.set_completer_delims(' \t\n;')
    readline.set_completer(complete_path)
    readline.parse_and_bind("tab: complete")

    # Initialize the token manager
    token_manager = TokenManager()

    # If user wants to delete the stored token, do so and exit
    if args.delete_token:
        success = token_manager.delete_token()
        sys.exit(0 if success else 1)

    # Prepare configuration
    output_dir = args.output or (Path("transcripts") / datetime.now().strftime("%Y%m%d"))
    config = TranscriptionConfig(
        output_directory=output_dir,
        whisper_model=args.whisper_model
    )

    # Initialize pipeline
    pipeline = TranscriptionPipeline(config)
    hf_token = args.token or get_token(token_manager)
    if not hf_token:
        logger.error("No Hugging Face token provided. Exiting.")
        sys.exit(1)

    # Initialize models
    if not pipeline.initialize_models(hf_token):
        logger.error("Failed to initialize pipeline. Exiting.")
        sys.exit(1)

    # Prompt user for audio file path if not passed in
    audio_path = args.audio
    while not audio_path or not audio_path.exists():
        audio_path_str = input("\nEnter path to audio file (Tab for autocomplete): ").strip()
        audio_path = Path(audio_path_str)
        if not audio_path.exists():
            print(f"File '{audio_path}' not found. Please try again.")

    print("Audio file path accepted. Preparing to process the audio...")
    sys.stdout.flush()

    # Process the audio file
    if not pipeline.process_file(audio_path):
        sys.exit(1)


if __name__ == "__main__":
    main()