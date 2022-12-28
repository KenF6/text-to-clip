from difflib import SequenceMatcher
from typing import List, Tuple

from src.models.transcription.Transcript import Transcript


class SearchTermMatcher:
    def __init__(self):
        pass

    def find_sentence(self, sentence: str, transcript: Transcript) -> List[Tuple[int, int, int]]:
        indices = []
        words_in_transcript = transcript.full_text.split()
        sentence = sentence.split()

        for sentence_word_index, word_from_sentence in enumerate(sentence):
            for transcript_word_index, word_from_transcript in enumerate(words_in_transcript):
                if word_from_transcript == word_from_sentence:
                    number_of_words_remaining_in_transcript = len(words_in_transcript) - transcript_word_index

                    if number_of_words_remaining_in_transcript >= len(sentence):
                        sentence_in_transcript = words_in_transcript[
                                 transcript_word_index - sentence_word_index:transcript_word_index - sentence_word_index + len(
                                     sentence)]
                        s = SequenceMatcher(None, sentence_in_transcript, sentence)

                        if s.ratio() >= 0.4:
                            indices.append((transcript_word_index - sentence_word_index,
                                            transcript_word_index - sentence_word_index + len(sentence),
                                            s.ratio()))

        return self.deduplicate_tuples(indices)

    def deduplicate_tuples(self, tuples: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
        s = set()
        for t in tuples:
            s.add(t)
        return list(s)
