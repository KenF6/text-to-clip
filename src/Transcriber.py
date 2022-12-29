import json
import sys
from pathlib import PurePosixPath
from typing import Any

from vosk import Model, KaldiRecognizer

from src.MediaHandler import MediaHandler
from src.models.transcription.Transcript import Transcript


class Transcriber:
    def __init__(self, input_filepath: PurePosixPath):
        self.filepath: PurePosixPath = input_filepath
        self.original_input_media_handler: MediaHandler = MediaHandler(self.filepath)
        self.prepared_input_media_handler: MediaHandler = None

    def _create_prepared_filepath(self) -> PurePosixPath:
        filename: PurePosixPath = self.filepath.stem
        directory: PurePosixPath = self.filepath.parent
        return directory / PurePosixPath(f"{filename}_prepared.wav")

    def create_transcript(self) -> Transcript:
        if not self.is_format_supported():
            print("Audio file must be WAV format mono PCM.")
            sys.exit(1)

        recognizer = self.initialize_recognizer(lang="en-us")
        recognition_result = self.run_recognizer(recognizer)

        self.original_input_media_handler.close_wav_file()

        return Transcript.from_dict(json.loads(recognition_result))

    def is_format_supported(self) -> bool:
        wave_file = self.original_input_media_handler.read_wav_file()
        if wave_file.getnchannels() != 1 or wave_file.getsampwidth() != 2 or wave_file.getcomptype() != "NONE":
            return False
        return True

    def initialize_recognizer(self, lang: str) -> KaldiRecognizer:
        model = Model(lang="en-us")
        rec = KaldiRecognizer(model, self.original_input_media_handler.read_wav_file().getframerate())
        rec.SetWords(True)
        return rec

    def run_recognizer(self, recognizer: KaldiRecognizer) -> Any:
        while True:
            data = self.original_input_media_handler.read_wav_file().readframes(self.original_input_media_handler.read_wav_file().getnframes())
            if len(data) == 0:
                break
            else:
                recognizer.AcceptWaveform(data)

        final_result = recognizer.FinalResult()
        return final_result

