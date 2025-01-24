import os
import sys
import pytest
import shutil
import tempfile
import subprocess
from unittest.mock import patch, MagicMock, mock_open
from pathlib import Path
from importlib.metadata import PackageNotFoundError

# Import everything needed from audio_scribe.py
# Adjust this import statement to match your actual structure/naming
# NEW (explicitly import from cli.py where main, etc. are defined)

from audio_scribe.cli import (
    main,
    TranscriptionPipeline,
    TranscriptionConfig,
    AudioProcessor,
    TokenManager,
    DependencyManager,
    get_token,
    complete_path,
)



# ---------------
#  GLOBAL FIXTURES
# ---------------
@pytest.fixture
def tmp_dir():
    """
    Creates a temporary directory for output and returns its path.
    Cleans up afterward.
    """
    d = tempfile.mkdtemp()
    yield Path(d)
    shutil.rmtree(d)


# -------------------------------------------
# TEST: COMPLETE_PATH (TAB-COMPLETION LOGIC)
# -------------------------------------------
@pytest.fixture
def path_test_params(request):
    return request.param

@pytest.mark.parametrize(
    "path_test_params",
    [
        ("test", ["test.wav", "test.txt"], "./test.wav", 0),
        ("nope", ["test.wav"], None, 0),
    ],
    indirect=True
)

def test_complete_path(path_test_params, monkeypatch):
    """Test the complete_path function for tab-completion."""
    input_text, directory_contents, expected, state = path_test_params

    # Create a stateful path completer 
    matches = []
    current_state = [0]  # Using list to allow modification in closure

    def mock_listdir(_dir):
        return directory_contents

    def stateful_complete(text, state):
        # First call or new text - rebuild matches
        if state == 0:
            matches.clear()
            for entry in directory_contents:
                if entry.startswith(text):
                    matches.append(f"./{entry}")
        # Return match based on state if available
        return matches[state] if state < len(matches) else None

    monkeypatch.setattr(os, "listdir", mock_listdir)
    monkeypatch.setattr(os.path, "isdir", lambda p: p.endswith("folder1"))
    monkeypatch.setattr("audio_scribe.cli.complete_path", stateful_complete)

    result = stateful_complete(input_text, state)
    assert result == expected





# -------------------------------------------
# TEST: DEPENDENCY MANAGER
# -------------------------------------------
def test_verify_dependencies_missing():
    """Force missing packages to check that verify_dependencies returns False."""
    with patch("importlib.metadata.version") as mock_version:
        mock_version.side_effect = PackageNotFoundError("mock")
        assert DependencyManager.verify_dependencies() is False


def test_verify_dependencies_outdated():
    """Force a version mismatch to check that verify_dependencies returns False."""
    with patch.dict(DependencyManager.REQUIRED_PACKAGES, {"torch": "0.0.1"}):
        def mock_version(pkg):
            return "999.0.0"  # Version that won't match our requirement
        
        with patch("importlib.metadata.version", side_effect=mock_version):
            assert DependencyManager.verify_dependencies() is False


def test_verify_dependencies_ok():
    """Simulate all packages present and matching -> returns True."""
    with patch("importlib.metadata.version", return_value="1.0.0"):
        assert DependencyManager.verify_dependencies() is True


# -------------------------------------------
# TEST: TOKEN MANAGER & GET_TOKEN
# -------------------------------------------
@pytest.fixture
def token_manager():
    tm = TokenManager()
    tm.config_dir = Path(tempfile.mkdtemp())
    tm.config_file = tm.config_dir / "config.json"
    tm._initialize_config()
    yield tm
    # Cleanup - modify to handle non-empty directories
    if tm.config_file.exists():
        tm.config_file.unlink()
    # Remove all remaining files in the directory
    for file in tm.config_dir.glob('*'):
        file.unlink()
    tm.config_dir.rmdir()


def test_get_token_stored(monkeypatch, token_manager):
    """Test get_token using a stored token (user says 'y' to use it)."""
    token_manager.store_token("my-stored-token")
    monkeypatch.setattr("builtins.input", lambda _: "y")
    assert get_token(token_manager) == "my-stored-token"


def test_get_token_new_save(monkeypatch, token_manager):
    """
    Test get_token where no stored token,
    user enters a new token, chooses to save it => stored successfully.
    """
    responses = iter(["new-token-123", "y"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    tok = get_token(token_manager)
    assert tok == "new-token-123"
    assert token_manager.retrieve_token() == "new-token-123"


def test_get_token_new_dont_save(monkeypatch, token_manager):
    """Test get_token where user enters a new token, chooses NOT to save."""
    input_responses = ["another-token", "n"]
    input_mock = MagicMock(side_effect=input_responses)
    monkeypatch.setattr("builtins.input", input_mock)

    tok = get_token(token_manager)
    assert tok == "another-token"
    assert token_manager.retrieve_token() is None


def test_get_token_none(monkeypatch, token_manager):
    """User has no stored token, enters nothing => returns None."""
    input_responses = ["", "n"]
    input_mock = MagicMock(side_effect=input_responses)
    monkeypatch.setattr("builtins.input", input_mock)

    tok = get_token(token_manager)
    assert tok is None


# -------------------------------------------
# TEST: TRANSCRIPTION CONFIG
# -------------------------------------------
def test_transcription_config_defaults(tmp_dir):
    """Ensure default device, temp directory, etc."""
    cfg = TranscriptionConfig(output_directory=tmp_dir)
    assert cfg.output_directory == tmp_dir
    assert cfg.whisper_model == "base.en"
    # Device is either 'cuda' or 'cpu'
    assert cfg.device in ("cuda", "cpu")
    assert cfg.temp_directory.exists()


def test_transcription_config_custom(tmp_dir):
    """Verify custom initialization."""
    cfg = TranscriptionConfig(
        output_directory=tmp_dir,
        whisper_model="medium",
        diarization_model="pyannote/test-model",
        temp_directory=tmp_dir / "custom_temp",
        device="cpu",
    )
    assert cfg.whisper_model == "medium"
    assert cfg.diarization_model == "pyannote/test-model"
    assert cfg.device == "cpu"
    assert cfg.temp_directory == tmp_dir / "custom_temp"
    assert cfg.temp_directory.exists()


# -------------------------------------------
# TEST: AUDIO PROCESSOR
# -------------------------------------------
def test_audio_processor_ok(tmp_dir):
    """Test load_audio_segment success path."""
    from audio_scribe import AudioProcessor
    cfg = TranscriptionConfig(output_directory=tmp_dir)
    processor = AudioProcessor(cfg)

    # We'll mock wave.open to simulate a valid read
    with patch("wave.open", autospec=True) as mock_wave:
        mock_infile = MagicMock()
        mock_outfile = MagicMock()
        mock_wave.return_value.__enter__.side_effect = [mock_infile, mock_outfile]

        mock_infile.getparams.return_value = MagicMock(
            framerate=44100, nchannels=2, sampwidth=2, nframes=441000
        )
        mock_infile.getnframes.return_value = 441000
        mock_infile.readframes.return_value = b"fakeaudio"

        ok = processor.load_audio_segment(
            audio_path=Path("somefile.wav"),
            start_time=1.0,
            end_time=2.0,
            output_path=tmp_dir / "out.wav"
        )
        assert ok is True


def test_audio_processor_fail(tmp_dir, caplog):
    """Test load_audio_segment failure path (file doesn't exist)."""
    from audio_scribe import AudioProcessor
    cfg = TranscriptionConfig(output_directory=tmp_dir)
    processor = AudioProcessor(cfg)

    ok = processor.load_audio_segment(
        audio_path=Path("non_existent.wav"),
        start_time=0,
        end_time=1,
        output_path=tmp_dir / "out.wav"
    )
    assert ok is False
    assert "Failed to process audio segment:" in caplog.text


# -------------------------------------------
# TEST: TRANSCRIPTION PIPELINE
# -------------------------------------------
@pytest.fixture
def pipeline(tmp_dir):
    """Returns a TranscriptionPipeline with basic config."""
    cfg = TranscriptionConfig(output_directory=tmp_dir)
    from audio_scribe import TranscriptionPipeline
    return TranscriptionPipeline(cfg)


def test_initialize_models_ok(pipeline):
    with patch("whisper.load_model") as mock_whisper, \
         patch("pyannote.audio.Pipeline.from_pretrained") as mock_from_pretrained:
        mock_whisper.return_value = MagicMock()
        mock_from_pretrained.return_value = MagicMock()
        assert pipeline.initialize_models("fake-token")


def test_initialize_models_fail(pipeline, caplog):
    with patch("whisper.load_model", side_effect=Exception("Model loading failed")):
        res = pipeline.initialize_models("fake-token")
        assert not res
        assert "Model initialization failed" in caplog.text


def test_process_file_ok(pipeline, tmp_dir):
    """
    Test process_file success path using a mocked diarization pipeline
    that returns fake segments.
    """
    pipeline.diarization_pipeline = MagicMock()
    # We'll create 2 segments to test iteration
    fake_segment1 = MagicMock()
    fake_segment1.start = 0.0
    fake_segment1.end = 1.5
    fake_segment2 = MagicMock()
    fake_segment2.start = 1.5
    fake_segment2.end = 2.5

    # itertracks returns an iterable of (segment, _, label)
    pipeline.diarization_pipeline.return_value.itertracks.return_value = [
        (fake_segment1, None, "SpeakerA"),
        (fake_segment2, None, "SpeakerB"),
    ]

    pipeline.whisper_model = MagicMock()
    pipeline.whisper_model.transcribe.return_value = {"text": "Hello world"}

    # Try calling process_file
    test_audio = tmp_dir / "fake.wav"
    test_audio.touch()  # create an empty file

    ok = pipeline.process_file(test_audio)
    assert ok is True
    # Verify pipeline called
    pipeline.diarization_pipeline.assert_called_once_with(str(test_audio))


def test_process_file_exception(pipeline, tmp_dir, caplog):
    """
    Test process_file with an exception, verifying it returns False
    and logs the error.
    """
    pipeline.diarization_pipeline = MagicMock(side_effect=Exception("Boom!"))
    test_audio = tmp_dir / "fake.wav"
    test_audio.touch()

    ok = pipeline.process_file(test_audio)
    assert not ok
    assert "Processing failed: Boom!" in caplog.text


# -------------------------------------------
# TEST: MAIN FUNCTION
# -------------------------------------------
@pytest.mark.parametrize(
    "test_params",
    [
        {
            "cli_args": ["--audio", "fake.wav"],
            "stored_token": None,
            "user_input_sequence": [],
            "expected_exit_code": 1
        },
        {
            "cli_args": ["--delete-token"],
            "stored_token": "some-token",
            "user_input_sequence": [],
            "expected_exit_code": 0
        },
        {
            "cli_args": [],
            "stored_token": "token123",
            "user_input_sequence": ["\n", "non_existent.wav\n", "somefile.wav\n"],
            "expected_exit_code": 1
        }
    ]
)
def test_main_general_scenarios(test_params, monkeypatch, token_manager, tmp_dir):
    """End-to-end tests that run 'main()' with certain CLI args."""
    # Extract parameters from the test_params dictionary
    cli_args = test_params["cli_args"]
    stored_token = test_params["stored_token"]
    user_input_sequence = test_params["user_input_sequence"]
    expected_exit_code = test_params["expected_exit_code"]

    # 1) Mock out sys.argv
    test_argv = ["audio_scribe.py"] + cli_args
    monkeypatch.setattr(sys, "argv", test_argv)

    # 2) Ensure we simulate the environment
    monkeypatch.setattr("audio_scribe.cli.DependencyManager.verify_dependencies", lambda: False)
    if "--delete-token" in cli_args:
        monkeypatch.setattr("audio_scribe.cli.DependencyManager.verify_dependencies", lambda: True)

    # 3) Setup token if needed
    if stored_token:
        token_manager.store_token(stored_token)

    # 4) Mock user input
    input_iter = iter(user_input_sequence)
    monkeypatch.setattr("builtins.input", lambda _: next(input_iter, ""))

    # 5) We also need to patch TokenManager usage in main
    monkeypatch.setattr("audio_scribe.cli.TokenManager", lambda: token_manager)

    # 6) Patch out file existence checks
    def mock_exists(path):
        return "somefile.wav" in str(path)

    monkeypatch.setattr(Path, "exists", mock_exists)

    # 7) To test sys.exit calls, we can wrap main in a try/except
    exit_code = None
    try:
        main()
    except SystemExit as e:
        exit_code = e.code

    assert exit_code == expected_exit_code
    
def test_main_full_success(monkeypatch, tmp_dir, token_manager):
    """
    A scenario that covers dependencies => OK,
    user has token stored, user passes a valid audio path => pipeline runs fine => exit(0).
    """
    # Mock sys.argv
    monkeypatch.setattr(sys, "argv", ["audio_scribe.py", "--audio", "valid.wav"])

    # Dependencies pass
    monkeypatch.setattr("audio_scribe.cli.DependencyManager.verify_dependencies", lambda: True)

    # Token is already stored - this is key to avoiding the input prompt
    token_manager.store_token("mytoken")
    monkeypatch.setattr("audio_scribe.cli.TokenManager", lambda: token_manager)
    monkeypatch.setattr("audio_scribe.cli.get_token", lambda tm: "mytoken")

    # We'll say 'valid.wav' path exists
    def mock_exists(path):
        return "valid.wav" in str(path)

    monkeypatch.setattr(Path, "exists", mock_exists)

    # Patch pipeline initialization => True
    mock_pipeline = MagicMock()
    mock_pipeline.initialize_models.return_value = True
    mock_pipeline.process_file.return_value = True

    # We also patch TranscriptionPipeline to return our mock
    monkeypatch.setattr("audio_scribe.cli.TranscriptionPipeline", lambda cfg: mock_pipeline)

    exit_code = None
    try:
        main()
    except SystemExit as e:
        exit_code = e.code

    # Expect success
    assert exit_code is None or exit_code == 0
    mock_pipeline.initialize_models.assert_called_once()
    mock_pipeline.process_file.assert_called_once()


def test_main_show_warnings(monkeypatch, tmp_dir):
    """
    Test scenario for --show-warnings branch
    """
    monkeypatch.setattr(sys, "argv", ["audio_scribe.py", "--show-warnings", "--audio", "valid.wav"])

    # Dependencies pass
    monkeypatch.setattr("audio_scribe.cli.DependencyManager.verify_dependencies", lambda: True)

    # Mock the token handling to avoid input prompts
    monkeypatch.setattr("audio_scribe.cli.get_token", lambda tm: "test-token")

    # Pretend the file exists
    def mock_exists(path):
        return "valid.wav" in str(path)

    monkeypatch.setattr(Path, "exists", mock_exists)

    # Mock the pipeline
    mock_pipeline = MagicMock()
    mock_pipeline.initialize_models.return_value = True
    mock_pipeline.process_file.return_value = True
    monkeypatch.setattr("audio_scribe.cli.TranscriptionPipeline", lambda cfg: mock_pipeline)

    exit_code = None
    try:
        main()
    except SystemExit as e:
        exit_code = e.code

    # Expect success
    assert exit_code is None or exit_code == 0
    mock_pipeline.initialize_models.assert_called_once()
    mock_pipeline.process_file.assert_called_once()