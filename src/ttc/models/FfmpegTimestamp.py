from datetime import time, timedelta


class FfmpegTimestamp:
    def __init__(self, duration: timedelta) -> None:
        self.timestamp: time = duration

    def get_formatted_timestamp(self):
        return str(self.timestamp)
