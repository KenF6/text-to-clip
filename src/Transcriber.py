import json
import sys
from pathlib import PurePosixPath
from typing import Any

from vosk import Model, KaldiRecognizer

from src.MediaHandler import MediaHandler
from src.models.transcription.Transcript import Transcript


class Transcriber:
    def __init__(self, input_filepath: PurePosixPath):
        self.filepath = input_filepath
        self.media_handler = MediaHandler(self.filepath)

    def create_transcript(self) -> Transcript:
        if not self.is_format_supported():
            print("Audio file must be WAV format mono PCM.")
            sys.exit(1)

        recognizer = self.initialize_recognizer(lang="en-us")
        recognition_result = self.run_recognizer(recognizer)

        self.media_handler.close_wav_file()

        return Transcript.from_dict(json.loads(recognition_result))

    def is_format_supported(self) -> bool:
        wave_file = self.media_handler.read_wav_file()
        if wave_file.getnchannels() != 1 or wave_file.getsampwidth() != 2 or wave_file.getcomptype() != "NONE":
            return False
        return True

    def initialize_recognizer(self, lang: str) -> KaldiRecognizer:
        model = Model(lang="en-us")
        rec = KaldiRecognizer(model, self.media_handler.read_wav_file().getframerate())
        rec.SetWords(True)
        return rec

    def run_recognizer(self, recognizer: KaldiRecognizer) -> Any:
        while True:
            data = self.media_handler.read_wav_file().readframes(self.media_handler.read_wav_file().getnframes())
            if len(data) == 0:
                break
            else:
                recognizer.AcceptWaveform(data)

        final_result = recognizer.FinalResult()
        return final_result

