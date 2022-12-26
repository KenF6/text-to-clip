import pytest

from src.TextHelper import TextHelper


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        ("One, Two?",
         "one two"),
        ("",
         "")
    ]
)
def test_normalize_text(test_input: str, expected_output: str):
    # Act
    output = TextHelper.normalize_text(test_input)

    # Assert
    assert output == expected_output


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        (["apple", "banana", "cherry"],
         "apple_banana_cherry"),
        ([],
         "")
    ]
)
def test_join_strings_with_underscores(test_input: list[str], expected_output: str):
    # Act
    output = TextHelper.join_strings_with_underscores(test_input)

    # Assert
    assert output == expected_output


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        ("./test_files/transcripts/test_transcript.txt", "This is a test transcript.\n")
    ]
)
def test_read_transcript(test_input: str, expected_output: str):
    # Act
    output = TextHelper.read_transcript(test_input)

    # Assert
    assert output == expected_output


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        ("This is a test transcript. This transcript has duplicate words.",
         ["this", "is", "a", "test", "transcript", "has", "duplicate", "words"])
    ]
)
def test_sanitize_transcript(test_input: str, expected_output: list[str]):
    # Act
    output = TextHelper.sanitize_transcript(test_input)

    # Assert
    assert sorted(output) == sorted(expected_output)


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        ("This is a test transcript.", ["this", "is", "a", "test", "transcript"])
    ]
)
def test_turn_text_into_plain_word_list(test_input: str, expected_output: list[str]):
    # Act
    output = TextHelper.turn_text_into_plain_word_list(test_input)

    # Assert
    assert output == expected_output


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        (["This", "is", "a", "test", "transcript!"], ["this", "is", "a", "test", "transcript"])
    ]
)
def test_remove_all_punctuation(test_input: list[str], expected_output: list[str]):
    # Act
    output = TextHelper.remove_all_punctuation(test_input)

    # Assert
    assert output == expected_output
