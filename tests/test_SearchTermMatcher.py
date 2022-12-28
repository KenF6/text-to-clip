from typing import List, Tuple, Set

import pytest

from src.SearchTermMatcher import SearchTermMatcher
from src.models.matching.PotentialMatch import PotentialMatch
from src.models.transcription.RecognizedWord import RecognizedWord
from src.models.transcription.Transcript import Transcript


@pytest.mark.parametrize(
    "search_term, transcript, expected_matches",
    [
        ("ever since his remarkable disappearance and unexpected return",
         Transcript(
             words=[RecognizedWord(conf=1.0, end=3.81, start=3.48, text='book'),
                    RecognizedWord(conf=1.0, end=4.32, start=3.84, text='one'),
                    RecognizedWord(conf=1.0, end=6.66, start=6.24, text='chapter'),
                    RecognizedWord(conf=1.0, end=7.11, start=6.66, text='one'),
                    RecognizedWord(conf=0.726133, end=8.31, start=8.22, text='a'),
                    RecognizedWord(conf=0.726133, end=8.73, start=8.31, text='long'),
                    RecognizedWord(conf=1.0, end=9.385529, start=8.73, text='expected'),
                    RecognizedWord(conf=0.738834, end=10.05, start=9.395273, text='ponting'),
                    RecognizedWord(conf=1.0, end=13.26, start=13.05, text='when'),
                    RecognizedWord(conf=0.588733, end=13.560001, start=13.260001, text='mr'),
                    RecognizedWord(conf=1.0, end=14.07, start=13.560001, text='bilbo'),
                    RecognizedWord(conf=1.0, end=14.61, start=14.07, text='baggins'),
                    RecognizedWord(conf=0.438313, end=14.67, start=14.61, text='a'),
                    RecognizedWord(conf=1.0, end=15.0, start=14.710316, text='bag'),
                    RecognizedWord(conf=1.0, end=15.36, start=15.0, text='and'),
                    RecognizedWord(conf=1.0, end=16.11, start=15.63, text='announced'),
                    RecognizedWord(conf=1.0, end=16.26, start=16.11, text='that'),
                    RecognizedWord(conf=1.0, end=16.35, start=16.26, text='he'),
                    RecognizedWord(conf=0.790888, end=16.5, start=16.35, text='will'),
                    RecognizedWord(conf=1.0, end=16.92, start=16.53, text='shortly'),
                    RecognizedWord(conf=1.0, end=17.04, start=16.92, text='be'),
                    RecognizedWord(conf=1.0, end=17.73, start=17.04, text='celebrating'),
                    RecognizedWord(conf=0.896383, end=17.88, start=17.73, text='his'),
                    RecognizedWord(conf=0.568641, end=18.24982, start=17.88, text='eleven'),
                    RecognizedWord(conf=0.487162, end=18.35968, start=18.25125, text='the'),
                    RecognizedWord(conf=1.0, end=18.72, start=18.35968, text='first'),
                    RecognizedWord(conf=1.0, end=19.29, start=18.75, text='birthday'),
                    RecognizedWord(conf=1.0, end=19.74, start=19.53, text='with'),
                    RecognizedWord(conf=1.0, end=19.8, start=19.74, text='a'),
                    RecognizedWord(conf=1.0, end=20.22, start=19.8, text='party'),
                    RecognizedWord(conf=1.0, end=20.31, start=20.22, text='of'),
                    RecognizedWord(conf=1.0, end=20.82, start=20.31, text='special'),
                    RecognizedWord(conf=1.0, end=21.63, start=20.82, text='magnificence'),
                    RecognizedWord(conf=1.0, end=22.29, start=22.11, text='there'),
                    RecognizedWord(conf=1.0, end=22.44, start=22.29, text='was'),
                    RecognizedWord(conf=1.0, end=22.77, start=22.44, text='much'),
                    RecognizedWord(conf=1.0, end=23.25, start=22.83, text='talk'),
                    RecognizedWord(conf=1.0, end=23.37, start=23.25, text='and'),
                    RecognizedWord(conf=1.0, end=23.97065, start=23.37, text='excitement'),
                    RecognizedWord(conf=0.791833, end=24.09, start=23.97065, text='in'),
                    RecognizedWord(conf=0.437091, end=24.57, start=24.09, text='hospital'),
                    RecognizedWord(conf=0.414803, end=26.07, start=25.74, text='bill'),
                    RecognizedWord(conf=0.643974, end=26.31, start=26.097263, text='though'),
                    RecognizedWord(conf=1.0, end=26.58, start=26.31, text='was'),
                    RecognizedWord(conf=0.699251, end=26.880002, start=26.640002, text='that'),
                    RecognizedWord(conf=0.699251, end=27.120002, start=26.880002, text='era'),
                    RecognizedWord(conf=1.0, end=27.9, start=27.69, text='and'),
                    RecognizedWord(conf=1.0, end=28.23, start=27.9, text='very'),
                    RecognizedWord(conf=1.0, end=28.86, start=28.23, text='peculiar'),
                    RecognizedWord(conf=1.0, end=29.58, start=29.43, text='and'),
                    RecognizedWord(conf=1.0, end=29.67, start=29.58, text='had'),
                    RecognizedWord(conf=1.0, end=29.88, start=29.67, text='been'),
                    RecognizedWord(conf=1.0, end=30.0, start=29.88, text='the'),
                    RecognizedWord(conf=0.72002, end=30.269998, start=30.0, text='one'),
                    RecognizedWord(conf=0.72002, end=30.443914, start=30.269998, text='that'),
                    RecognizedWord(conf=1.0, end=30.51, start=30.443914, text='of'),
                    RecognizedWord(conf=1.0, end=30.63, start=30.51, text='the'),
                    RecognizedWord(conf=1.0, end=31.02, start=30.63, text='shire'),
                    RecognizedWord(conf=1.0, end=31.17, start=31.02, text='for'),
                    RecognizedWord(conf=1.0, end=31.59, start=31.17, text='sixty'),
                    RecognizedWord(conf=1.0, end=32.1, start=31.59, text='years'),
                    RecognizedWord(conf=1.0, end=32.97, start=32.73, text='ever'),
                    RecognizedWord(conf=1.0, end=33.24, start=32.97, text='since'),
                    RecognizedWord(conf=1.0, end=33.39, start=33.24, text='his'),
                    RecognizedWord(conf=1.0, end=34.14, start=33.39, text='remarkable'),
                    RecognizedWord(conf=1.0, end=34.95, start=34.14, text='disappearance'),
                    RecognizedWord(conf=1.0, end=35.22, start=35.04, text='and'),
                    RecognizedWord(conf=1.0, end=35.88, start=35.22, text='unexpected'),
                    RecognizedWord(conf=0.565717, end=36.39, start=35.88, text='return'),
                    RecognizedWord(conf=1.0, end=37.86, start=37.59, text='that'),
                    RecognizedWord(conf=1.0, end=38.31, start=37.86, text='reaches'),
                    RecognizedWord(conf=1.0, end=38.43, start=38.31, text='he'),
                    RecognizedWord(conf=1.0, end=38.55, start=38.43, text='had'),
                    RecognizedWord(conf=1.0, end=38.88, start=38.55, text='brought'),
                    RecognizedWord(conf=1.0, end=39.18, start=38.91, text='back'),
                    RecognizedWord(conf=1.0, end=39.36, start=39.18, text='from'),
                    RecognizedWord(conf=1.0, end=39.48, start=39.36, text='his'),
                    RecognizedWord(conf=1.0, end=39.9, start=39.48, text='travels'),
                    RecognizedWord(conf=1.0, end=40.35, start=40.2, text='had'),
                    RecognizedWord(conf=0.846971, end=40.68, start=40.35, text='now'),
                    RecognizedWord(conf=1.0, end=41.04, start=40.68, text='become'),
                    RecognizedWord(conf=1.0, end=41.1, start=41.04, text='a'),
                    RecognizedWord(conf=1.0, end=41.64, start=41.1, text='local'),
                    RecognizedWord(conf=1.0, end=42.27, start=41.64, text='legend'),
                    RecognizedWord(conf=1.0, end=42.96, start=42.69, text='and'),
                    RecognizedWord(conf=1.0, end=43.08, start=42.96, text='it'),
                    RecognizedWord(conf=1.0, end=43.29, start=43.08, text='was'),
                    RecognizedWord(conf=1.0, end=43.95, start=43.29, text='popularly'),
                    RecognizedWord(conf=1.0, end=44.55, start=43.95, text='believed'),
                    RecognizedWord(conf=1.0, end=45.33, start=44.91, text='whatever'),
                    RecognizedWord(conf=1.0, end=45.45, start=45.33, text='the'),
                    RecognizedWord(conf=1.0, end=45.69, start=45.45, text='old'),
                    RecognizedWord(conf=1.0, end=45.93, start=45.69, text='folk'),
                    RecognizedWord(conf=1.0, end=46.17, start=45.93, text='might'),
                    RecognizedWord(conf=1.0, end=46.44, start=46.17, text='say'),
                    RecognizedWord(conf=1.0, end=47.16, start=46.95, text='that'),
                    RecognizedWord(conf=1.0, end=47.28, start=47.16, text='the'),
                    RecognizedWord(conf=1.0, end=47.55052, start=47.28, text='hill'),
                    RecognizedWord(conf=0.320941, end=47.64, start=47.55052, text='at'),
                    ],

             full_text="book one chapter one a long expected ponting when mr bilbo baggins a bag and announced that he will shortly "
                       "be celebrating his eleven the first birthday with a party of special magnificence there was much talk and "
                       "excitement in hospital bill though was that era and very peculiar and had been the one that of the shire "
                       "for sixty years ever since his remarkable disappearance and unexpected return that reaches he had brought "
                       "back from his travels had now become a local legend and it was popularly believed whatever the old folk "
                       "might say that the hill at",
         ),
         [PotentialMatch(words=[RecognizedWord(conf=1.0, end=32.97, start=32.73, text='ever'),
                                RecognizedWord(conf=1.0, end=33.24, start=32.97, text='since'),
                                RecognizedWord(conf=1.0, end=33.39, start=33.24, text='his'),
                                RecognizedWord(conf=1.0, end=34.14, start=33.39, text='remarkable'),
                                RecognizedWord(conf=1.0, end=34.95, start=34.14, text='disappearance'),
                                RecognizedWord(conf=1.0, end=35.22, start=35.04, text='and'),
                                RecognizedWord(conf=1.0, end=35.88, start=35.22, text='unexpected'),
                                RecognizedWord(conf=0.565717, end=36.39, start=35.88, text='return')],
                         confidence=1.0)]
         )
    ]
)
def test_find_potential_matches(search_term: str, transcript: Transcript, expected_matches: List[PotentialMatch]):
    # Arrange
    matcher = SearchTermMatcher()

    # Act
    matches_found = matcher.find_potential_matches(search_term, transcript)

    # Assert
    assert matches_found == expected_matches
