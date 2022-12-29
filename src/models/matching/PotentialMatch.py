from dataclasses import dataclass
from datetime import timedelta
from typing import List

from src.models.FfmpegTimestamp import FfmpegTimestamp
from src.models.transcription.RecognizedWord import RecognizedWord


@dataclass
class PotentialMatch:
    words: List[RecognizedWord]
    confidence: float

    def get_start(self):
        start = self.words[0].start
        start_timestamp = timedelta(seconds=start)
        return FfmpegTimestamp(start_timestamp)

    def get_end(self):
        end = self.words[-1].end
        end_timestamp = timedelta(seconds=end)
        return FfmpegTimestamp(end_timestamp)