from dataclasses import dataclass
from typing import Any


@dataclass
class Tags:
    DURATION: str
    ENCODER: str

    @staticmethod
    def from_dict(obj: Any) -> 'Tags':
        _DURATION = str(obj.get("DURATION"))
        _ENCODER = str(obj.get("ENCODER"))
        return Tags(_DURATION, _ENCODER)
