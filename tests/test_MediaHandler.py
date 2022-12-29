import os
from datetime import time
from pathlib import PurePosixPath

import ffmpeg
import pytest

from src.MediaHandler import MediaHandler
from src.models.FfmpegTimestamp import FfmpegTimestamp
from src.models.media_info.AudioStream import AudioStream
from src.models.media_info.Disposition import Disposition
from src.models.media_info.Format import Format
from src.models.media_info.MediaInfo import MediaInfo
from src.models.media_info.Tags import Tags
from src.models.media_info.VideoStream import VideoStream


@pytest.mark.parametrize(
    "input_file, expected_output_file",
    [
        ("./test_files/mb_monte_carlo/tests_prepared/cut-Money Boy - Monte Carlo 360p.mp4",
         "./test_files/tests_temp/cut-Money Boy - Monte Carlo 360p.wav"),
        ("./test_files/mb_monte_carlo/tests_prepared/cut-Money Boy - Monte Carlo 480p.mp4",
         "./test_files/tests_temp/cut-Money Boy - Monte Carlo 480p.wav")
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
    assert audio_stream['codec_name'] == 'wav'


@pytest.mark.parametrize(
    "input_file, expected_output_file",
    [
        ("./test_files/mb_monte_carlo/tests_prepared/cut-Money Boy - Monte Carlo 360p.mp4",
         "./test_files/tests_temp/cut-Money Boy - Monte Carlo 360p.wav"),
        ("./test_files/mb_monte_carlo/tests_prepared/cut-Money Boy - Monte Carlo 480p.mp4",
         "./test_files/tests_temp/cut-Money Boy - Monte Carlo 480p.wav")
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


@pytest.mark.parametrize(
    "input_file, expected_result",
    [
        ("./test_files/mb_monte_carlo/tests_prepared/cut-Money Boy - Monte Carlo 360p.mp4",
         MediaInfo(video_streams=[
             VideoStream(index=0, codec_name='h264', codec_long_name='H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10',
                         profile='Main', codec_type='video', codec_tag_string='avc1', codec_tag='0x31637661', width=640,
                         height=360, coded_width=640, coded_height=360, closed_captions=0, has_b_frames=1,
                         sample_aspect_ratio='1:1', display_aspect_ratio='16:9', pix_fmt='yuv420p', level=30,
                         color_range='tv', color_space='bt709', refs=1, r_frame_rate='25/1', avg_frame_rate='25/1',
                         time_base='1/12800', start_pts=0, start_time='0.000000',
                         disposition=Disposition(default=1, dub=0, original=0, comment=0, lyrics=0, karaoke=0, forced=0,
                                                 hearing_impaired=0, visual_impaired=0, clean_effects=0, attached_pic=0,
                                                 timed_thumbnails=0, captions=0, descriptions=0, metadata=0,
                                                 dependent=0, still_image=0),
                         tags=Tags(DURATION='None', ENCODER='None'))], audio_streams=[
             AudioStream(index=1, codec_name='aac', codec_long_name='AAC (Advanced Audio Coding)', codec_type='audio',
                         codec_tag_string='mp4a', codec_tag='0x6134706d', sample_fmt='fltp', sample_rate='44100',
                         channels=2, channel_layout='stereo', bits_per_sample=0, r_frame_rate='0/0',
                         avg_frame_rate='0/0', time_base='1/44100', start_pts=0, start_time='0',
                         disposition=Disposition(default=1, dub=0, original=0, comment=0, lyrics=0, karaoke=0, forced=0,
                                                 hearing_impaired=0, visual_impaired=0, clean_effects=0, attached_pic=0,
                                                 timed_thumbnails=0, captions=0, descriptions=0, metadata=0,
                                                 dependent=0, still_image=0), tags=None)], format=Format(
             filename='ignore-filename',
             nb_streams=2, nb_programs=0, format_name='mov,mp4,m4a,3gp,3g2,mj2', format_long_name='QuickTime / MOV',
             start_time='0.000000', duration='5.080000', size='408222', bit_rate='642869', probe_score=100,
             tags=Tags(DURATION='None', ENCODER='None')))
         )
    ]
)
def test_get_media_info(input_file, expected_result):
    # Arrange
    path_to_current_file = os.path.realpath(__file__)
    current_directory = os.path.dirname(path_to_current_file)

    input_path = PurePosixPath(current_directory) / PurePosixPath(input_file)

    media_handler = MediaHandler(input_path)

    # Act
    media_info = media_handler.get_media_info()

    # Assert
    media_info.format.filename = 'ignore-filename'
    expected_result.filename = 'ignore-filename'
    assert media_info == expected_result
