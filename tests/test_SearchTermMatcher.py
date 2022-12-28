from typing import List, Tuple

import pytest

from src.SearchTermMatcher import SearchTermMatcher


@pytest.mark.parametrize(
    "transcribed_text, search_term, expected_output",
    [
        ("book one chapter one a long expected ponting when mr bilbo baggins a bag and announced that he will shortly "
         "be celebrating his eleven the first birthday with a party of special magnificence there was much talk and "
         "excitement in hospital bill though was that era and very peculiar and had been the one that of the shire "
         "for sixty years ever since his remarkable disappearance and unexpected return that reaches he had brought "
         "back from his travels had now become a local legend and it was popularly believed whatever the old folk "
         "might say that the hill at bag and was full of tunnels stuffed with treasure and if that was not enough for "
         "fame there was also he's prolonged bigger to marvel at time what on that it seemed to have little effect on "
         "mister beckons at ninety he was much the same as at fifty at ninety nine they began to call him well "
         "preserved but unchanged would have been near them are there was some the shook their heads and thought this "
         "was too much of a good thing it seemed unfair that anyone should possess a patently perpetual youth as well "
         "as reputedly inexhaustible will it will have to be paid for they said it isn't natural and trouble will "
         "come of it that so far troubled had not come and as mr baggins was generous with his money most people were "
         "willing to forgive him his oddities and his good fortune he remained on visiting terms with his relatives "
         "except of course the sackville baggins as and he had many devoted admired as among the hobby to poor and "
         "unimportant families but he had",
         "at ninety he was much the same as at fifty",
         [(138, 148, 1.0), (140, 150, 0.8)]
         )
    ]
)
def test_find_sentence(transcribed_text: str, search_term: str, expected_output: List[Tuple[int, int, int]]):
    # Arrange
    matcher = SearchTermMatcher()

    # Act
    output = matcher.find_sentence(search_term, transcribed_text)

    # Assert
    assert output == expected_output
