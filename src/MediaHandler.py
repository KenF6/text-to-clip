import os
from pathlib import PurePosixPath

import ffmpeg


class MediaHandler:
    def __init__(self, input_file: PurePosixPath):
        self.input_file: PurePosixPath = input_file

    def cut_and_save(self, output_file: PurePosixPath, start_time, end_time):
        if os.path.exists(output_file):
            os.remove(output_file)

        output = (
            ffmpeg
            .input(self.input_file.as_posix())
            .trim(start=start_time, end=end_time)
            .output(output_file.as_posix())
        )

        output.run()
