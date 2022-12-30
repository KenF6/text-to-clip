from dataclasses import dataclass
from typing import Any


@dataclass
class Disposition:
    default: int
    dub: int
    original: int
    comment: int
    lyrics: int
    karaoke: int
    forced: int
    hearing_impaired: int
    visual_impaired: int
    clean_effects: int
    attached_pic: int
    timed_thumbnails: int
    captions: int
    descriptions: int
    metadata: int
    dependent: int
    still_image: int

    @staticmethod
    def from_dict(obj: Any) -> 'Disposition':
        _default = int(obj.get("default"))
        _dub = int(obj.get("dub"))
        _original = int(obj.get("original"))
        _comment = int(obj.get("comment"))
        _lyrics = int(obj.get("lyrics"))
        _karaoke = int(obj.get("karaoke"))
        _forced = int(obj.get("forced"))
        _hearing_impaired = int(obj.get("hearing_impaired"))
        _visual_impaired = int(obj.get("visual_impaired"))
        _clean_effects = int(obj.get("clean_effects"))
        _attached_pic = int(obj.get("attached_pic"))
        _timed_thumbnails = int(obj.get("timed_thumbnails"))
        _captions = int(obj.get("captions"))
        _descriptions = int(obj.get("descriptions"))
        _metadata = int(obj.get("metadata"))
        _dependent = int(obj.get("dependent"))
        _still_image = int(obj.get("still_image"))
        return Disposition(_default, _dub, _original, _comment, _lyrics, _karaoke, _forced, _hearing_impaired,
                           _visual_impaired, _clean_effects, _attached_pic, _timed_thumbnails, _captions, _descriptions,
                           _metadata, _dependent, _still_image)
