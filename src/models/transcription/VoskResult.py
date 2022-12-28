from dataclasses import dataclass
from typing import Any
from typing import List

from src.models.transcription.VoskWord import VoskWord


@dataclass
class VoskResult:
    words: List[VoskWord]
    text: str

    @staticmethod
    def from_dict(obj: Any) -> 'VoskResult':
        _result = [VoskWord.from_dict(y) for y in obj.get("result")]
        _text = str(obj.get("text"))
        return VoskResult(_result, _text)
