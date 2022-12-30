import os
from pathlib import PurePosixPath

import pytest

from src.ttc.Transcriber import Transcriber
from src.ttc.models.transcription.Transcript import Transcript
from src.ttc.models.transcription.RecognizedWord import RecognizedWord


@pytest.mark.parametrize(
    "filepath, expected_output",
    [
        ("./test_files/clips/test_file_lotr_1.wav", Transcript(
            words=[RecognizedWord(conf=1.0, end=0.78, start=0.21, text='bilbo'),
                   RecognizedWord(conf=1.0, end=1.08, start=0.78, text='was'),
                   RecognizedWord(conf=0.78532, end=1.44, start=1.11, text='very'),
                   RecognizedWord(conf=0.39845, end=1.65, start=1.44, text='rich'),
                   RecognizedWord(conf=1.0, end=2.37, start=2.16, text='and'),
                   RecognizedWord(conf=1.0, end=2.7, start=2.37, text='very'),
                   RecognizedWord(conf=1.0, end=3.33, start=2.7, text='peculiar'),
                   RecognizedWord(conf=1.0, end=4.067259, start=3.9, text='and'),
                   RecognizedWord(conf=1.0, end=4.38, start=4.17, text='been'),
                   RecognizedWord(conf=1.0, end=4.47, start=4.38, text='the'),
                   RecognizedWord(conf=1.0, end=4.77, start=4.47, text='one'),
                   RecognizedWord(conf=1.0, end=4.92, start=4.77, text='that'),
                   RecognizedWord(conf=0.72296, end=5.01, start=4.92, text='of'),
                   RecognizedWord(conf=1.0, end=5.1, start=5.01, text='the'),
                   RecognizedWord(conf=1.0, end=5.52, start=5.1, text='shire'),
                   RecognizedWord(conf=1.0, end=5.64, start=5.52, text='for'),
                   RecognizedWord(conf=1.0, end=6.06, start=5.64, text='sixty'),
                   RecognizedWord(conf=1.0, end=6.6, start=6.06, text='years'),
                   RecognizedWord(conf=1.0, end=7.44, start=7.23, text='ever'),
                   RecognizedWord(conf=1.0, end=7.71, start=7.44, text='since'),
                   RecognizedWord(conf=1.0, end=7.86, start=7.71, text='his'),
                   RecognizedWord(conf=1.0, end=8.64, start=7.86, text='remarkable'),
                   RecognizedWord(conf=1.0, end=9.45, start=8.64, text='disappearance'),
                   RecognizedWord(conf=1.0, end=9.72, start=9.51, text='and'),
                   RecognizedWord(conf=1.0, end=10.35, start=9.72, text='unexpected'),
                   RecognizedWord(conf=0.503514, end=10.86, start=10.35, text='return')],
            full_text='bilbo was very rich and very peculiar and been the one that of the shire for sixty years ever '
                      'since his remarkable disappearance and unexpected return'))
    ]
)
def test_create_transcript(filepath: str, expected_output: Transcript):
    # Arrange
    path_to_current_file = os.path.realpath(__file__)
    current_directory = os.path.dirname(path_to_current_file)

    input_path = PurePosixPath(current_directory) / PurePosixPath(filepath)

    transcriber = Transcriber(PurePosixPath(input_path))

    # Act
    output = transcriber.create_transcript()

    # Assert
    assert output == expected_output


@pytest.mark.parametrize(
    "input_filepath, expected_filepath",
    [
        (PurePosixPath("/c/some/folder/somefile.somextension"),
         PurePosixPath("/c/some/folder/somefile_prepared.wav")),
        (PurePosixPath("C:\\some\\folder\\somefile.somextension"),
         PurePosixPath("C:\\some\\folder\\somefile_prepared.wav"))
    ]
)
def test_create_prepared_filepath(input_filepath: PurePosixPath, expected_filepath: PurePosixPath):
    # Arrange
    transcriber = Transcriber(input_filepath)

    # Act
    prepared_filepath = transcriber._create_prepared_filepath()

    # Assert
    assert prepared_filepath == expected_filepath
