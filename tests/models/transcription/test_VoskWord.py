import pytest

from src.ttc.models.transcription.RecognizedWord import RecognizedWord


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        ({
            "start": 0.5,
            "end": 1.6,
            "word": "car",
            "conf": 0.3
         }, RecognizedWord(conf=0.3, start=0.5, end=1.6, text="car")),
        ({
            "start": 0.0,
            "end": 1.5,
            "word": "train",
            "conf": 0.6
         }, RecognizedWord(conf=0.6, start=0.0, end=1.5, text="train"))
    ]
)
def test_from_dict(test_input: dict, expected_output: RecognizedWord):
    # Act
    output = RecognizedWord.from_dict(test_input)

    # Assert
    assert output == expected_output
