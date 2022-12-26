from datetime import time


class FfmpegTimestamp:
    def __init__(self, duration: time) -> None:
        self.timestamp: time = duration

    def get_formatted_timestamp(self):
        return self.timestamp.isoformat(timespec='seconds')
