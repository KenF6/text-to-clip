import os
from pathlib import PurePosixPath

import pytest

from src.Transcriber import Transcriber
from src.models.transcription.VoskResult import VoskResult
from src.models.transcription.VoskWord import VoskWord


@pytest.mark.parametrize(
    "filepath, expected_output",
    [
        ("./test_files/clips/test_file_lotr_1.wav", VoskResult(
            words=[VoskWord(conf=1.0, end=0.78, start=0.21, word='bilbo'),
                   VoskWord(conf=1.0, end=1.08, start=0.78, word='was'),
                   VoskWord(conf=0.78532, end=1.44, start=1.11, word='very'),
                   VoskWord(conf=0.39845, end=1.65, start=1.44, word='rich'),
                   VoskWord(conf=1.0, end=2.37, start=2.16, word='and'),
                   VoskWord(conf=1.0, end=2.7, start=2.37, word='very'),
                   VoskWord(conf=1.0, end=3.33, start=2.7, word='peculiar'),
                   VoskWord(conf=1.0, end=4.067259, start=3.9, word='and'),
                   VoskWord(conf=1.0, end=4.38, start=4.17, word='been'),
                   VoskWord(conf=1.0, end=4.47, start=4.38, word='the'),
                   VoskWord(conf=1.0, end=4.77, start=4.47, word='one'),
                   VoskWord(conf=1.0, end=4.92, start=4.77, word='that'),
                   VoskWord(conf=0.72296, end=5.01, start=4.92, word='of'),
                   VoskWord(conf=1.0, end=5.1, start=5.01, word='the'),
                   VoskWord(conf=1.0, end=5.52, start=5.1, word='shire'),
                   VoskWord(conf=1.0, end=5.64, start=5.52, word='for'),
                   VoskWord(conf=1.0, end=6.06, start=5.64, word='sixty'),
                   VoskWord(conf=1.0, end=6.6, start=6.06, word='years'),
                   VoskWord(conf=1.0, end=7.44, start=7.23, word='ever'),
                   VoskWord(conf=1.0, end=7.71, start=7.44, word='since'),
                   VoskWord(conf=1.0, end=7.86, start=7.71, word='his'),
                   VoskWord(conf=1.0, end=8.64, start=7.86, word='remarkable'),
                   VoskWord(conf=1.0, end=9.45, start=8.64, word='disappearance'),
                   VoskWord(conf=1.0, end=9.72, start=9.51, word='and'),
                   VoskWord(conf=1.0, end=10.35, start=9.72, word='unexpected'),
                   VoskWord(conf=0.503514, end=10.86, start=10.35, word='return')],
            text='bilbo was very rich and very peculiar and been the one that of the shire for sixty years ever since '
                 'his remarkable disappearance and unexpected return'))
    ]
)
def test_create_transcript(filepath: str, expected_output: VoskResult):
    # Arrange
    path_to_current_file = os.path.realpath(__file__)
    current_directory = os.path.dirname(path_to_current_file)

    input_path = PurePosixPath(current_directory) / PurePosixPath(filepath)

    transcriber = Transcriber(PurePosixPath(input_path))

    # Act
    output = transcriber.create_transcript()

    # Assert
    assert output == expected_output
