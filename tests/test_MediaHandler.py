import os
from datetime import time
from pathlib import PurePosixPath

import ffmpeg
import pytest

from src.MediaHandler import MediaHandler
from src.models.FfmpegTimestamp import FfmpegTimestamp


@pytest.mark.parametrize(
    "input_file, expected_output_file",
    [
        ("./test_files/mb_monte_carlo/tests_prepared/cut-Money Boy - Monte Carlo 360p.mp4",
         "./test_files/tests_temp/cut-Money Boy - Monte Carlo 360p.aac"),
        ("./test_files/mb_monte_carlo/tests_prepared/cut-Money Boy - Monte Carlo 480p.mp4",
         "./test_files/tests_temp/cut-Money Boy - Monte Carlo 480p.aac")
    ]
)
def test_save_prepared_for_transcription(input_file: str,
                                         expected_output_file: str):
    # Arrange
    path_to_current_file = os.path.realpath(__file__)
    current_directory = os.path.dirname(path_to_current_file)

    input_path = PurePosixPath(current_directory) / PurePosixPath(input_file)
    output_path = PurePosixPath(current_directory) / PurePosixPath(expected_output_file)

    if os.path.exists(output_path):
        os.remove(output_path)

    media_handler = MediaHandler(input_path)

    # Act
    media_handler.save_prepared_for_transcription(output_path)

    # Assert
    probe = ffmpeg.probe(expected_output_file)

    audio_stream = next(s for s in probe['streams'] if s['codec_type'] == 'audio')
    assert audio_stream['sample_rate'] == '16000'
    assert audio_stream['channel_layout'] == 'mono'
    assert audio_stream['codec_name'] == 'aac'


@pytest.mark.parametrize(
    "input_file, expected_output_file",
    [
        ("./test_files/mb_monte_carlo/tests_prepared/cut-Money Boy - Monte Carlo 360p.mp4",
         "./test_files/tests_temp/cut-Money Boy - Monte Carlo 360p.aac"),
        ("./test_files/mb_monte_carlo/tests_prepared/cut-Money Boy - Monte Carlo 480p.mp4",
         "./test_files/tests_temp/cut-Money Boy - Monte Carlo 480p.aac")
    ]
)
def test_save_prepared_for_transcription(input_file: str,
                                         expected_output_file: str):
    # Arrange
    path_to_current_file = os.path.realpath(__file__)
    current_directory = os.path.dirname(path_to_current_file)

    input_path = PurePosixPath(current_directory) / PurePosixPath(input_file)
    output_path = PurePosixPath(current_directory) / PurePosixPath(expected_output_file)

    if os.path.exists(output_path):
        os.remove(output_path)

    media_handler = MediaHandler(input_path)

    # Act
    media_handler.save_prepared_for_transcription(output_path)

    # Assert
    assert os.path.exists(output_path)


@pytest.mark.parametrize(
    "input_file, output_file, start_time, end_time, expected_duration",
    [
        ("./test_files/mb_monte_carlo/tests_prepared/cut-Money Boy - Monte Carlo 360p.mp4",
         "./test_files/tests_temp/cut-Money Boy - Monte Carlo 360p.mp4",
         FfmpegTimestamp(time(hour=0, minute=0, second=0)),
         FfmpegTimestamp(time(hour=0, minute=0, second=4)),
         4.0),
        ("./test_files/mb_monte_carlo/tests_prepared/cut-Money Boy - Monte Carlo 480p.mp4",
         "./test_files/tests_temp/cut-Money Boy - Monte Carlo 480p.mp4",
         FfmpegTimestamp(time(hour=0, minute=0, second=2)),
         FfmpegTimestamp(time(hour=0, minute=0, second=6))
         , 5.08)
    ]
)
def test_cut_and_save_file_is_created(input_file: str,
                                      output_file: str,
                                      start_time: FfmpegTimestamp,
                                      end_time: FfmpegTimestamp,
                                      expected_duration: float):
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


@pytest.mark.parametrize(
    "input_file, output_file, start_time, end_time, expected_duration",
    [
        ("./test_files/mb_monte_carlo/tests_prepared/cut-Money Boy - Monte Carlo 360p.mp4",
         "./test_files/tests_temp/cut-Money Boy - Monte Carlo 360p.mp4",
         FfmpegTimestamp(time(hour=0, minute=0, second=0)),
         FfmpegTimestamp(time(hour=0, minute=0, second=4)),
         4.0),
        ("./test_files/mb_monte_carlo/tests_prepared/cut-Money Boy - Monte Carlo 480p.mp4",
         "./test_files/tests_temp/cut-Money Boy - Monte Carlo 480p.mp4",
         FfmpegTimestamp(time(hour=0, minute=0, second=2)),
         FfmpegTimestamp(time(hour=0, minute=0, second=6))
         , 5.08)
    ]
)
def test_cut_and_save_duration_is_correct(input_file: str,
                                          output_file: str,
                                          start_time: FfmpegTimestamp,
                                          end_time: FfmpegTimestamp,
                                          expected_duration: float):
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
    probe = ffmpeg.probe(output_path)
    duration = float(probe['format']['duration'])
    assert duration == expected_duration
