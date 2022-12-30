from dataclasses import dataclass
from typing import Any

from src.ttc.models.media_info.Tags import Tags


@dataclass
class Format:
    filename: str
    nb_streams: int
    nb_programs: int
    format_name: str
    format_long_name: str
    start_time: str
    duration: str
    size: str
    bit_rate: str
    probe_score: int
    tags: Tags

    @staticmethod
    def from_dict(obj: Any) -> 'Format':
        _filename = str(obj.get("filename"))
        _nb_streams = int(obj.get("nb_streams"))
        _nb_programs = int(obj.get("nb_programs"))
        _format_name = str(obj.get("format_name"))
        _format_long_name = str(obj.get("format_long_name"))
        _start_time = str(obj.get("start_time"))
        _duration = str(obj.get("duration"))
        _size = str(obj.get("size"))
        _bit_rate = str(obj.get("bit_rate"))
        _probe_score = int(obj.get("probe_score"))
        _tags = Tags.from_dict(obj.get("tags"))
        return Format(_filename, _nb_streams, _nb_programs, _format_name, _format_long_name, _start_time, _duration,
                      _size, _bit_rate, _probe_score, _tags)
