import os
import wave
from pathlib import PurePosixPath
from typing import Union

import ffmpeg

from src.models.FfmpegTimestamp import FfmpegTimestamp
from src.models.media_info.MediaInfo import MediaInfo


class MediaHandler:
    def __init__(self, input_file: PurePosixPath):
        self.input_file: PurePosixPath = input_file
        self.wav_handle: Union[wave.Wave_write, wave.Wave_read] = None

    def cut_and_save(self, output_file: PurePosixPath, start_time: FfmpegTimestamp, end_time: FfmpegTimestamp):
        if os.path.exists(output_file):
            os.remove(output_file)

        info = ffmpeg.probe(self.input_file.as_posix())
        streams = info['streams']

        codec_types: list[str] = []
        for stream in streams:
            if stream['codec_type'] not in codec_types:
                codec_types.append(stream['codec_type'])

        output_streams = []

        input_file = ffmpeg.input(self.input_file.as_posix())

        has_audio = 'audio' in codec_types
        has_video = 'video' in codec_types

        if has_audio:
            audio_stream = input_file.audio
            trimmed_audio_stream = audio_stream.filter('atrim', start=start_time.get_formatted_timestamp(),
                                                       end=end_time.get_formatted_timestamp())
            output_streams.append(trimmed_audio_stream)

        if has_video:
            vid_stream = input_file.video
            trimmed_video_stream = vid_stream \
                .trim(start=start_time.get_formatted_timestamp(), end=end_time.get_formatted_timestamp())
            output_streams.append(trimmed_video_stream)

        output_video_and_audio = ffmpeg.output(*output_streams, output_file.as_posix())

        output_video_and_audio.overwrite_output().run()

    def save_prepared_for_transcription(self, output_file: PurePosixPath):
        audio_stream = (
            ffmpeg
                .input(self.input_file.as_posix())
                .audio
                .filter('aformat', channel_layouts='mono', sample_rates='16000')
                .output(output_file.as_posix(), acodec='aac')
        )

        audio_stream.run()

    def get_media_info(self) -> MediaInfo:
        info = ffmpeg.probe(self.input_file.as_posix())
        return MediaInfo.from_dict(info)

    def read_wav_file(self) -> Union[wave.Wave_write, wave.Wave_read]:
        if self.wav_handle is None:
            self.wav_handle = wave.open(self.input_file.as_posix(), "rb")
        return self.wav_handle

    def close_wav_file(self) -> None:
        if self.wav_handle is not None:
            self.wav_handle.close()
