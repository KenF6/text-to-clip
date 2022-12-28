from dataclasses import dataclass
from typing import Any


@dataclass
class RecognizedWord:
    conf: float
    end: float
    start: float
    text: str

    @staticmethod
    def from_dict(obj: Any) -> 'RecognizedWord':
        _conf = float(obj.get("conf"))
        _end = float(obj.get("end"))
        _start = float(obj.get("start"))
        _text = str(obj.get("word"))
        return RecognizedWord(_conf, _end, _start, _text)

    def __str__(self) -> str:
        """
        Returns a string representation of the RecognizedWord object.
        """
        return f"VoskWord(conf={self.conf}, end={self.end}, start={self.start}, text='{self.text}')"



