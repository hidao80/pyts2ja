# pyts2ja

Transcribe text from mp3 or m4a files.

## Description

This script converts mp3 or m4a audio files into text by transcribing the spoken content. It supports transcription in Japanese using Google's speech recognition service.

## Features

- Converts `mp3` and `m4a` audio files into `wav` format for processing.
- Transcribes audio content in Japanese (`ja-JP`).
- Uses Google's speech recognition API for accurate transcription.
- Simple to use with command-line input.

## Requirements

- Python 3.6 or higher
- Required Python libraries:
  - `speech_recognition`
  - `pydub`
- `ffmpeg` installed and accessible in your system's PATH for audio format conversion.

## Installation

1. Install Python dependencies:
   ```bash
   pip install speechrecognition pydub
   ```
2. Install `ffmpeg` for audio processing:
   - Refer to the [FFmpeg official documentation](https://ffmpeg.org/download.html) for installation instructions.

## Usage

Run the script with the path to your audio file as an argument:

```bash
python ts2ja.py <path_to_audio_file>
```

### Example

```bash
python ts2ja.py example.mp3
```

## Error Handling

- If the file format is not supported, the script will prompt an error message.
- If transcription fails, detailed error messages will be provided:
  - `"Could not understand the audio."`
  - `"Could not access the speech recognition service."`

## Notes

- The script deletes temporary files automatically after processing.
- Only Japanese transcription (`ja-JP`) is supported.

## License

This project is open-source and available under the [MIT License](LICENSE).
