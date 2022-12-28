import os
import wave
from pathlib import PurePosixPath
from typing import Union

import ffmpeg

from src.models.FfmpegTimestamp import FfmpegTimestamp


class MediaHandler:
    def __init__(self, input_file: PurePosixPath):
        self.input_file: PurePosixPath = input_file
        self.wav_handle: Union[wave.Wave_write, wave.Wave_read] = None

    def cut_and_save(self, output_file: PurePosixPath, start_time: FfmpegTimestamp, end_time: FfmpegTimestamp):
        if os.path.exists(output_file):
            os.remove(output_file)

        vid_stream = ffmpeg.input(self.input_file).video
        audio_stream = ffmpeg.input(self.input_file).audio

        trimmed_video_stream = vid_stream \
            .trim(start=start_time.get_formatted_timestamp(), end=end_time.get_formatted_timestamp())

        trimmed_audio_stream = audio_stream.filter('atrim', start=start_time.get_formatted_timestamp(),
                                                   end=end_time.get_formatted_timestamp())

        output_video_and_audio = ffmpeg.output(trimmed_video_stream, trimmed_audio_stream,
                                               output_file.as_posix())

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

    def read_wav_file(self) -> Union[wave.Wave_write, wave.Wave_read]:
        if self.wav_handle is None:
            self.wav_handle = wave.open(self.input_file.as_posix(), "rb")
        return self.wav_handle

    def close_wav_file(self) -> None:
        if self.wav_handle is not None:
            self.wav_handle.close()
