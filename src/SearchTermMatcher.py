from difflib import SequenceMatcher
from typing import List, Tuple, Set

from src.TextHelper import TextHelper
from src.models.matching.PotentialMatch import PotentialMatch
from src.models.transcription.Transcript import Transcript


class SearchTermMatcher:
    def __init__(self):
        self.text_helper = TextHelper()

    def find_potential_matches(self, sentence: str, transcript: Transcript) -> List[PotentialMatch]:
        potential_matches: List[PotentialMatch] = []
        sentence = self.text_helper.turn_text_into_plain_word_list(sentence)

        for sentence_word_index, word_from_sentence in enumerate(sentence):
            for transcript_word_index, word_from_transcript in enumerate(transcript.words):
                if word_from_transcript.text == word_from_sentence:
                    number_of_words_remaining_in_transcript = len(transcript.words) - transcript_word_index

                    if number_of_words_remaining_in_transcript >= len(sentence):
                        trying_to_match = transcript.words[
                                          transcript_word_index - sentence_word_index:transcript_word_index - sentence_word_index + len(
                                              sentence)]

                        trying_to_match_text = [word.text for word in trying_to_match]

                        s = SequenceMatcher(None, trying_to_match_text, sentence)

                        if s.ratio() >= 0.4:
                            potential_match = PotentialMatch(words=trying_to_match, confidence=s.ratio())
                            if potential_match not in potential_matches:
                                potential_matches.append(potential_match)

        return potential_matches