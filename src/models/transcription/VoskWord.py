from dataclasses import dataclass
from typing import Any


@dataclass
class VoskWord:
    conf: float
    end: float
    start: float
    word: str

    @staticmethod
    def from_dict(obj: Any) -> 'VoskWord':
        _conf = float(obj.get("conf"))
        _end = float(obj.get("end"))
        _start = float(obj.get("start"))
        _word = str(obj.get("word"))
        return VoskWord(_conf, _end, _start, _word)

    def __str__(self) -> str:
        """
        Returns a string representation of the VoskWord object.
        """
        return f"VoskWord(conf={self.conf}, end={self.end}, start={self.start}, word='{self.word}')"



