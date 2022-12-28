from dataclasses import dataclass
from typing import List

from src.models.transcription.RecognizedWord import RecognizedWord


@dataclass
class PotentialMatch:
    words: List[RecognizedWord]
    confidence: float
