import os
from pathlib import PurePosixPath

import ffmpeg

from src.models.FfmpegTimestamp import FfmpegTimestamp


class MediaHandler:
    def __init__(self, input_file: PurePosixPath):
        self.input_file: PurePosixPath = input_file

    def cut_and_save(self, output_file: PurePosixPath, start_time: FfmpegTimestamp, end_time: FfmpegTimestamp):
        if os.path.exists(output_file):
            os.remove(output_file)

        output = (
            ffmpeg
            .input(self.input_file.as_posix())
            .trim(start=start_time.get_formatted_timestamp(), end=end_time.get_formatted_timestamp())
            .output(output_file.as_posix())
        )

        output.run()
