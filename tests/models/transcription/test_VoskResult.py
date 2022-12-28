import pytest

from src.models.transcription.VoskResult import VoskResult
from src.models.transcription.VoskWord import VoskWord


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
         VoskResult(
             [
                 VoskWord(conf=0.3, start=0.5, end=1.6, word="car"),
                 VoskWord(conf=0.6, start=0.0, end=1.5, word="train")
             ],
             text="car train"))
    ])
def test_from_dict(test_input: dict, expected_output: VoskResult):
    # Act
    output = VoskResult.from_dict(test_input)

    # Assert
    assert output == expected_output
