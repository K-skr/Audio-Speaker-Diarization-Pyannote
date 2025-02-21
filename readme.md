# Audio Speaker Diarization

A Python-based speaker diarization system that leverages pyannote.audio to identify and separate different speakers in audio recordings. This tool helps analyze audio files by determining who spoke when.

## Features

- Speaker identification in audio recordings
- Integration with pyannote.audio 3.1
- Easy-to-use interface with Hugging Face models
- Support for various audio formats
- Audio file manipulation with pydub

## Prerequisites

- Python 3.8 or higher
- pyannote.audio 3.1
- pydub
- FFmpeg
- Hugging Face account and access token

## Installation

1. Clone the repository:
```bash
git clone https://github.com/K-skr/Audio-Speaker-Diarization-Pyannote.git
cd Audio-Speaker-Diarization-Pyannote.git
```

2. Install dependencies:
```bash
pip install pyannote.audio==3.1
pip install pydub
```

3. Install FFmpeg (required for pydub):

#### For Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

#### For macOS:
```bash
brew install ffmpeg
```

#### For Windows:
1. Download FFmpeg:
   - Go to [FFmpeg's official website](https://ffmpeg.org/download.html)
   - Click on "Windows Builds"
   - Download the latest build from gyan.dev or BtbN
   - Extract the zip file

2. Add FFmpeg to System PATH:
   - Copy the extracted folder to a permanent location (e.g., `C:\Program Files\ffmpeg`)
   - Open System Properties (Win + Pause|Break or right-click on This PC → Properties)
   - Click on "Advanced system settings"
   - Click on "Environment Variables"
   - Under "System Variables", find and select "Path"
   - Click "Edit"
   - Click "New"
   - Add the path to the FFmpeg bin folder (e.g., `C:\Program Files\ffmpeg\bin`)
   - Click "OK" on all windows

3. Verify installation:
   - Open a new Command Prompt
   - Type `ffmpeg -version`
   - If you see FFmpeg version information, the installation was successful

## Hugging Face Setup

### 1. Account Creation
- Create an account at [huggingface.co](https://huggingface.co) if you don't have one

### 2. Model Access
Accept the user conditions for these models:
- [pyannote/segmentation-3.0](https://huggingface.co/pyannote/segmentation-3.0)
- [pyannote/speaker-diarization-3.1](https://huggingface.co/pyannote/speaker-diarization-3.1)

### 3. Access Token
1. Navigate to [Hugging Face Settings](https://huggingface.co/settings/tokens)
2. Click "New token"
3. Name your token
4. Copy the generated token

### 4. Token Configuration
Add your HF token to the `HF_TOKEN` variable in the `main.py` file.
## Usage

Run the main script:
```bash
python main.py
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgments

- [pyannote.audio](https://github.com/pyannote/pyannote-audio) for the underlying audio processing capabilities
- [pydub](https://github.com/jiaaro/pydub) for audio file manipulation
- Hugging Face for model hosting and distribution

## Support

For support, please open an issue in the repository or contact [Your Contact Information].
