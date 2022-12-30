import json
from pathlib import PurePosixPath
from typing import Any

from vosk import Model, KaldiRecognizer

from src.ttc.MediaHandler import MediaHandler
from src.ttc.models.transcription.Transcript import Transcript


class Transcriber:
    def __init__(self, input_filepath: PurePosixPath):
        self.original_file: PurePosixPath = input_filepath
        self.prepared_file: PurePosixPath = None
        self.original_input_media_handler: MediaHandler = MediaHandler(self.original_file)
        self.prepared_input_media_handler: MediaHandler = None

    def create_transcript(self) -> Transcript:
        self._ensure_format_is_supported()

        recognizer = self._initialize_recognizer(lang="en-us")
        recognition_result = self._run_recognizer(recognizer)

        self.prepared_input_media_handler.close_wav_file()

        return Transcript.from_dict(json.loads(recognition_result))

    def _ensure_format_is_supported(self) -> None:
        if self._is_format_supported():
            self.prepared_file = self.original_file
            self.prepared_input_media_handler = self.original_input_media_handler

        else:
            self.prepared_file = self._create_prepared_filepath()
            self.original_input_media_handler.save_prepared_for_transcription(self.prepared_file)
            self.prepared_input_media_handler = MediaHandler(self.prepared_file)

    def _create_prepared_filepath(self) -> PurePosixPath:
        filename: PurePosixPath = self.original_file.stem
        directory: PurePosixPath = self.original_file.parent
        return directory / PurePosixPath(f"{filename}_prepared.wav")

    def _is_format_supported(self) -> bool:
        media_info = self.original_input_media_handler.get_media_info()
        if media_info.format.nb_streams != 1 \
                or media_info.format.format_name != 'wav' \
                or media_info.audio_streams[0].channels != 1 \
                or media_info.audio_streams[0].codec_name != 'pcm_s16le':
            return False
        return True

    def _initialize_recognizer(self, lang: str) -> KaldiRecognizer:
        model = Model(lang="en-us")
        rec = KaldiRecognizer(model, self.prepared_input_media_handler.read_wav_file().getframerate())
        rec.SetWords(True)
        return rec

    def _run_recognizer(self, recognizer: KaldiRecognizer) -> Any:
        while True:
            data = self.prepared_input_media_handler.read_wav_file().readframes(
                self.prepared_input_media_handler.read_wav_file().getnframes())
            if len(data) == 0:
                break
            else:
                recognizer.AcceptWaveform(data)

        final_result = recognizer.FinalResult()
        return final_result
