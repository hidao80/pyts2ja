import speech_recognition as sr
from pydub import AudioSegment
import sys
import os

# Get the path of the audio file from the command line arguments
if len(sys.argv) < 2:
    print("Please specify the path of the audio file.")
    sys.exit(1)

audio_file_path = sys.argv[1]
file_extension = os.path.splitext(audio_file_path)[1].lower()

# Convert MP3 or M4A to WAV
if file_extension == ".mp3":
    audio = AudioSegment.from_mp3(audio_file_path)
elif file_extension == ".m4a":
    audio = AudioSegment.from_file(audio_file_path, format="m4a")
else:
    print("Unsupported file format. Please specify an MP3 or M4A file.")
    sys.exit(1)

temp_wav_path = "converted_audio.wav"
audio.export(temp_wav_path, format="wav")

# Speech recognition
recognizer = sr.Recognizer()
with sr.AudioFile(temp_wav_path) as source:
    audio_data = recognizer.record(source)

try:
    # Transcription in Japanese
    transcript = recognizer.recognize_google(audio_data, language="ja-JP")
    print("Transcription:", transcript)
except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError:
    print("Could not access the speech recognition service.")
finally:
    # Delete the temporary file
    os.remove(temp_wav_path)
