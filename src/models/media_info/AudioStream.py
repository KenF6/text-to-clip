from dataclasses import dataclass
from typing import Any

from src.models.media_info.Disposition import Disposition
from src.models.media_info.Tags import Tags


@dataclass
class AudioStream:
    index: int
    codec_name: str
    codec_long_name: str
    codec_type: str
    codec_tag_string: str
    codec_tag: str
    sample_fmt: str
    sample_rate: str
    channels: int
    channel_layout: str
    bits_per_sample: int
    r_frame_rate: str
    avg_frame_rate: str
    time_base: str
    start_pts: int
    start_time: str
    disposition: Disposition
    tags: Tags

    @staticmethod
    def from_dict(obj: Any) -> 'AudioStream':
        _index = int(obj.get("index"))
        _codec_name = str(obj.get("codec_name"))
        _codec_long_name = str(obj.get("codec_long_name"))
        _codec_type = str(obj.get("codec_type"))
        _codec_tag_string = str(obj.get("codec_tag_string"))
        _codec_tag = str(obj.get("codec_tag"))
        _sample_fmt = str(obj.get("sample_fmt"))
        _sample_rate = str(obj.get("sample_rate"))
        _channels = int(obj.get("channels"))
        _channel_layout = str(obj.get("channel_layout"))
        _bits_per_sample = int(obj.get("bits_per_sample"))
        _r_frame_rate = str(obj.get("r_frame_rate"))
        _avg_frame_rate = str(obj.get("avg_frame_rate"))
        _time_base = str(obj.get("time_base"))
        _start_pts = int(obj.get("start_pts"))
        _start_time = str(obj.get("start_time"))
        _disposition = Disposition.from_dict(obj.get("disposition"))
        _tags = Tags.from_dict(obj.get("tags"))
        return AudioStream(_index, _codec_name, _codec_long_name, _codec_type, _codec_tag_string, _codec_tag, _sample_fmt, _sample_rate, _channels, _channel_layout, _bits_per_sample, _r_frame_rate, _avg_frame_rate, _time_base, _start_pts, _start_time, _disposition, _tags)