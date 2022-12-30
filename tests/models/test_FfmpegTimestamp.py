from datetime import time

import pytest

from src.ttc.models.FfmpegTimestamp import FfmpegTimestamp


@pytest.mark.parametrize(
    "create_timestamp_from, expected_string",
    [
        (time(hour=1, minute=22, second=16), "01:22:16"),
        (time(hour=5, minute=5, second=5), "05:05:05"),
        (time(hour=12, minute=2, second=00), "12:02:00")
    ]
)
def test_get_formatted_timestamp(create_timestamp_from: time, expected_string: str):
    # Arrange
    timestamp = FfmpegTimestamp(create_timestamp_from)

    # Act
    result = timestamp.get_formatted_timestamp()

    # Assert
    assert result == expected_string

