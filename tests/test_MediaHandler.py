import os
from pathlib import PurePosixPath

import ffmpeg
import pytest

from src.MediaHandler import MediaHandler


@pytest.mark.parametrize(
    "input_file, output_file, start_time, end_time, expected_duration",
    [
        ("./test_files/mb_monte_carlo/tests_prepared/cut-Money Boy - Monte Carlo 360p.mp4",
         "./test_files/tests_temp/cut-Money Boy - Monte Carlo 360p.mp4",
         "00:00:01", "00:00:04", 4.0),
        ("./test_files/mb_monte_carlo/tests_prepared/cut-Money Boy - Monte Carlo 480p.mp4",
         "./test_files/tests_temp/cut-Money Boy - Monte Carlo 480p.mp4", "00:00:02", "00:00:06", 5.08)
    ]
)
def test_cut_and_save_file_is_created(input_file, output_file, start_time, end_time, expected_duration):
    # Arrange
    path_to_current_file = os.path.realpath(__file__)
    current_directory = os.path.dirname(path_to_current_file)

    input_path = PurePosixPath(current_directory) / PurePosixPath(input_file)
    output_path = PurePosixPath(current_directory) / PurePosixPath(output_file)

    if os.path.exists(output_path):
        os.remove(output_path)

    media_handler = MediaHandler(input_path)

    # Act
    media_handler.cut_and_save(output_path, start_time, end_time)

    # Assert
    assert os.path.exists(output_path)

    probe = ffmpeg.probe(output_path)
    duration = float(probe['format']['duration'])
    assert duration == expected_duration


@pytest.mark.parametrize(
    "input_file, output_file, start_time, end_time, expected_duration",
    [
        ("./test_files/mb_monte_carlo/tests_prepared/cut-Money Boy - Monte Carlo 360p.mp4",
         "./test_files/tests_temp/cut-Money Boy - Monte Carlo 360p.mp4",
         "00:00:01", "00:00:04", 4.0),
        ("./test_files/mb_monte_carlo/tests_prepared/cut-Money Boy - Monte Carlo 480p.mp4",
         "./test_files/tests_temp/cut-Money Boy - Monte Carlo 480p.mp4", "00:00:02", "00:00:06", 5.08)
    ]
)
def test_cut_and_save_duration_is_correct(input_file, output_file, start_time, end_time, expected_duration):
    # Arrange
    path_to_current_file = os.path.realpath(__file__)
    current_directory = os.path.dirname(path_to_current_file)

    input_path = PurePosixPath(current_directory) / PurePosixPath(input_file)
    output_path = PurePosixPath(current_directory) / PurePosixPath(output_file)

    if os.path.exists(output_path):
        os.remove(output_path)

    media_handler = MediaHandler(input_path)

    # Act
    media_handler.cut_and_save(output_path, start_time, end_time)

    # Assert
    assert os.path.exists(output_path)

    probe = ffmpeg.probe(output_path)
    duration = float(probe['format']['duration'])
    assert duration == expected_duration
