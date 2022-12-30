from dataclasses import dataclass
from typing import List, Any

from src.ttc.models.media_info.AudioStream import AudioStream
from src.ttc.models.media_info.Format import Format
from src.ttc.models.media_info.VideoStream import VideoStream


@dataclass
class MediaInfo:
    video_streams: List[VideoStream]
    audio_streams: List[AudioStream]
    format: Format

    @staticmethod
    def from_dict(obj: Any) -> 'MediaInfo':
        _video_streams = [VideoStream.from_dict(y) for y in obj.get("streams") if y['codec_type'] == "video"]
        _audio_streams = [AudioStream.from_dict(y) for y in obj.get("streams") if y['codec_type'] == "audio"]
        _format = Format.from_dict(obj.get("format"))
        return MediaInfo(_video_streams, _audio_streams, _format)
