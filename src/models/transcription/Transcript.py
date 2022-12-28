from dataclasses import dataclass
from typing import Any
from typing import List

from src.models.transcription.RecognizedWord import RecognizedWord


@dataclass
class Transcript:
    words: List[RecognizedWord]
    full_text: str

    @staticmethod
    def from_dict(obj: Any) -> 'Transcript':
        _result = [RecognizedWord.from_dict(y) for y in obj.get("result")]
        _full_text = str(obj.get("text"))
        return Transcript(_result, _full_text)
