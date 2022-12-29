from dataclasses import dataclass
from typing import Any

from src.models.media_info.Disposition import Disposition
from src.models.media_info.Tags import Tags


@dataclass
class VideoStream:
    index: int
    codec_name: str
    codec_long_name: str
    profile: str
    codec_type: str
    codec_tag_string: str
    codec_tag: str
    width: int
    height: int
    coded_width: int
    coded_height: int
    closed_captions: int
    has_b_frames: int
    sample_aspect_ratio: str
    display_aspect_ratio: str
    pix_fmt: str
    level: int
    color_range: str
    color_space: str
    refs: int
    r_frame_rate: str
    avg_frame_rate: str
    time_base: str
    start_pts: int
    start_time: str
    disposition: Disposition
    tags: Tags

    @staticmethod
    def from_dict(obj: Any) -> 'VideoStream':
        _index = int(obj.get("index"))
        _codec_name = str(obj.get("codec_name"))
        _codec_long_name = str(obj.get("codec_long_name"))
        _profile = str(obj.get("profile"))
        _codec_type = str(obj.get("codec_type"))
        _codec_tag_string = str(obj.get("codec_tag_string"))
        _codec_tag = str(obj.get("codec_tag"))
        _width = int(obj.get("width"))
        _height = int(obj.get("height"))
        _coded_width = int(obj.get("coded_width"))
        _coded_height = int(obj.get("coded_height"))
        _closed_captions = int(obj.get("closed_captions"))
        _has_b_frames = int(obj.get("has_b_frames"))
        _sample_aspect_ratio = str(obj.get("sample_aspect_ratio"))
        _display_aspect_ratio = str(obj.get("display_aspect_ratio"))
        _pix_fmt = str(obj.get("pix_fmt"))
        _level = int(obj.get("level"))
        _color_range = str(obj.get("color_range"))
        _color_space = str(obj.get("color_space"))
        _refs = int(obj.get("refs"))
        _r_frame_rate = str(obj.get("r_frame_rate"))
        _avg_frame_rate = str(obj.get("avg_frame_rate"))
        _time_base = str(obj.get("time_base"))
        _start_pts = int(obj.get("start_pts"))
        _start_time = str(obj.get("start_time"))
        _disposition = Disposition.from_dict(obj.get("disposition"))
        _tags = Tags.from_dict(obj.get("tags"))
        return VideoStream(_index, _codec_name, _codec_long_name, _profile, _codec_type, _codec_tag_string, _codec_tag,
                           _width, _height, _coded_width, _coded_height, _closed_captions, _has_b_frames,
                           _sample_aspect_ratio, _display_aspect_ratio, _pix_fmt, _level, _color_range, _color_space, _refs,
                           _r_frame_rate, _avg_frame_rate, _time_base, _start_pts, _start_time, _disposition, _tags)
