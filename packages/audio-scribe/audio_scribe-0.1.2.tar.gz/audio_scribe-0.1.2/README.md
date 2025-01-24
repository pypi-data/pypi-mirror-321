# Audio Scribe

**A Command-Line Tool for Audio Transcription and Speaker Diarization Using OpenAI Whisper and Pyannote**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
![Coverage](https://img.shields.io/badge/coverage-94.3%25-brightgreen)
[![Pipeline Status](https://gitlab.genomicops.cloud/innovation-hub/audio-scribe/badges/main/pipeline.svg)](https://gitlab.genomicops.cloud/innovation-hub/audio-scribe/-/commits/main)
[![PyPI Version](https://badge.fury.io/py/audio-scribe.svg)](https://badge.fury.io/py/audio-scribe)
[![Python Versions](https://img.shields.io/pypi/pyversions/audio-scribe)](https://pypi.org/project/audio-scribe/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/audio-scribe)](https://pypi.org/project/audio-scribe/)
[![PyPI License](https://img.shields.io/pypi/l/audio-scribe)](https://pypi.org/project/audio-scribe/)
<!-- [![Coverage Report](https://gitlab.genomicops.cloud/innovation-hub/audio-scribe/badges/main/coverage.svg)](https://gitlab.genomicops.cloud/innovation-hub/audio-scribe/-/commits/main) -->

## Overview

**Audio Scribe** is a command-line tool that transcribes audio files with speaker diarization. Leveraging [OpenAI Whisper](https://github.com/openai/whisper) for transcription and [Pyannote Audio](https://github.com/pyannote/pyannote-audio) for speaker diarization, this solution converts audio into segmented text files, identifying each speaker turn. Key features include:

- **Progress Bar & Resource Monitoring**: See real-time CPU, memory, and GPU usage with a live progress bar.  
- **Speaker Diarization**: Automatically separates speaker turns using Pyannote’s state-of-the-art models.  
- **Tab-Completion for File Paths**: Easily navigate your file system when prompted for the audio path.  
- **Secure Token Storage**: Encrypts and stores your Hugging Face token for private model downloads.  
- **Customizable Whisper Models**: Default to `base.en`, or specify `tiny`, `small`, `medium`, `large`, etc.

This repository is licensed under the [Apache License 2.0](#license).

---

## Table of Contents

- [Audio Scribe](#audio-scribe)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
    - [Installing from PyPI](#installing-from-pypi)
    - [Installing from GitHub](#installing-from-github)
  - [Quick Start](#quick-start)
  - [Usage](#usage)
  - [Dependencies](#dependencies)
    - [Sample `requirements.txt`](#sample-requirementstxt)
  - [Contributing](#contributing)
  - [License](#license)

---

## Features

- **Whisper Transcription**  
  Utilizes [OpenAI Whisper](https://github.com/openai/whisper) to convert speech to text in multiple languages.  
- **Pyannote Speaker Diarization**  
  Identifies different speakers and segments your audio output accordingly.  
- **Progress Bar & Resource Usage**  
  Displays a live progress bar with CPU, memory, and GPU stats through [alive-progress](https://github.com/rsalmei/alive-progress), [psutil](https://pypi.org/project/psutil/), and [GPUtil](https://pypi.org/project/GPUtil/).  
- **Tab-Completion**  
  Press **Tab** to autocomplete file paths on Unix-like systems (and on Windows with [pyreadline3](https://pypi.org/project/pyreadline3/)).  
- **Secure Token Storage**  
  Saves your Hugging Face token via [cryptography](https://pypi.org/project/cryptography/) for model downloads (e.g., `pyannote/speaker-diarization-3.1`).  
- **Configurable Models**  
  Default is `base.en` but you can specify any other Whisper model using `--whisper-model`.

---

## Installation

### Installing from PyPI

**Audio Scribe** is available on PyPI. You can install it with:

```bash
pip install audio-scribe
```

After installation, the **`audio-scribe`** command should be available in your terminal (depending on how your PATH is configured). If you prefer to run via Python module, you can also do:

```bash
python -m audio-scribe --audio path/to/yourfile.wav
```

### Installing from GitHub

To install the latest development version directly from GitHub:

```bash
git clone https://gitlab.genomicops.cloud/genomicops/audio-scribe.git
cd audio-scribe
pip install -r requirements.txt
```

This approach is particularly useful if you want the newest changes or plan to contribute.

---

## Quick Start

1. **Obtain a Hugging Face Token**  
   - Create a token at [Hugging Face Settings](https://huggingface.co/settings/tokens).  
   - Accept the model conditions for `pyannote/segmentation-3.0` and `pyannote/speaker-diarization-3.1`.

2. **Run the Command-Line Tool**  
   ```bash
   audio-scribe --audio path/to/audio.wav
   ```
   > On the first run, you’ll be prompted for your Hugging Face token if you haven’t stored one yet.

3. **Watch the Progress Bar**  
   - The tool displays a progress bar for each diarized speaker turn, along with real-time CPU, GPU, and memory usage.

---

## Usage

Below is a summary of the main command-line options:

```
usage: audio-scribe [options]

Audio Transcription (Audio Scribe) Pipeline using Whisper + Pyannote, with optional progress bar.

optional arguments:
  --audio PATH           Path to the audio file to transcribe.
  --token TOKEN          HuggingFace API token. Overrides any saved token.
  --output PATH          Path to the output directory for transcripts and temporary files.
  --delete-token         Delete any stored Hugging Face token and exit.
  --show-warnings        Enable user warnings (e.g., from pyannote.audio). Disabled by default.
  --whisper-model MODEL  Specify the Whisper model to use (default: 'base.en').
```

**Examples:**

- **Basic Transcription**  
  ```bash
  audio-scribe --audio meeting.wav
  ```

- **Specify a Different Whisper Model**  
  ```bash
  audio-scribe --audio webinar.mp3 --whisper-model small
  ```

- **Delete a Stored Token**  
  ```bash
  audio-scribe --delete-token
  ```

- **Show Internal Warnings**  
  ```bash
  audio-scribe --audio session.wav --show-warnings
  ```

- **Tab-Completion**  
  ```bash
  audio-scribe
  # When prompted for an audio file path, press Tab to autocomplete
  ```

---

## Dependencies

**Core Libraries**  
- **Python 3.8+**  
- [PyTorch](https://pytorch.org/)  
- [openai-whisper](https://github.com/openai/whisper)  
- [pyannote.audio](https://github.com/pyannote/pyannote-audio)  
- [pytorch-lightning](https://pypi.org/project/pytorch-lightning/)  
- [cryptography](https://pypi.org/project/cryptography/)  
- [keyring](https://pypi.org/project/keyring/)  

**Optional for Extended Functionality**  
- [alive-progress](https://pypi.org/project/alive-progress/) – Real-time progress bar  
- [psutil](https://pypi.org/project/psutil/) – CPU/memory usage  
- [GPUtil](https://pypi.org/project/GPUtil/) – GPU usage  
- [pyreadline3](https://pypi.org/project/pyreadline3/) (for Windows tab-completion)

### Sample `requirements.txt`

Below is a typical `requirements.txt` you can place in your repository:

```
torch>=1.9
openai-whisper
pyannote.audio
pytorch-lightning
cryptography
keyring
alive-progress
psutil
GPUtil
pyreadline3; sys_platform == "win32"
```

> Note:  
> - `pyreadline3` is appended with a [PEP 508 marker](https://peps.python.org/pep-0508/) (`; sys_platform == "win32"`) so it only installs on Windows.  
> - For GPU support, ensure you install a compatible PyTorch version with CUDA.

---

## Contributing

We welcome contributions to **Audio Scribe**!

1. **Fork** the repository and clone your fork.  
2. **Create a new branch** for your feature or bugfix.  
3. **Implement your changes**, ensuring code is well-documented and follows best practices.  
4. **Open a pull request**, detailing the changes you’ve made.

Please read any available guidelines or templates in our repository (such as `CONTRIBUTING.md` or `CODE_OF_CONDUCT.md`) before submitting.

---

## License

This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

```
Copyright 2025 Gurasis Osahan

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

---

**Thank you for using Audio Scribe!**  
For questions or feedback, please open a [GitHub issue](https://gitlab.genomicops.cloud/genomicops/audio-scribe/issues) or contact the maintainers.