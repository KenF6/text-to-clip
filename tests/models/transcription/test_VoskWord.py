import pytest

from src.models.transcription.VoskWord import VoskWord


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        ({
            "start": 0.5,
            "end": 1.6,
            "word": "car",
            "conf": 0.3
         }, VoskWord(conf=0.3, start=0.5, end=1.6, word="car")),
        ({
            "start": 0.0,
            "end": 1.5,
            "word": "train",
            "conf": 0.6
         }, VoskWord(conf=0.6, start=0.0, end=1.5, word="train"))
    ]
)
def test_from_dict(test_input: dict, expected_output: VoskWord):
    # Act
    output = VoskWord.from_dict(test_input)

    # Assert
    assert output == expected_output
