import pytest

from src.models.transcription.Transcript import Transcript
from src.models.transcription.RecognizedWord import RecognizedWord


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        ({
             "result": [
                 {
                     "start": 0.5,
                     "end": 1.6,
                     "word": "car",
                     "conf": 0.3
                 },
                 {
                     "start": 0.0,
                     "end": 1.5,
                     "word": "train",
                     "conf": 0.6
                 }
             ],
             "text": "car train"
         },
         Transcript(
             [
                 RecognizedWord(conf=0.3, start=0.5, end=1.6, text="car"),
                 RecognizedWord(conf=0.6, start=0.0, end=1.5, text="train")
             ],
             full_text="car train"))
    ])
def test_from_dict(test_input: dict, expected_output: Transcript):
    # Act
    output = Transcript.from_dict(test_input)

    # Assert
    assert output == expected_output
