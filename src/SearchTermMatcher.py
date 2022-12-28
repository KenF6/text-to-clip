from difflib import SequenceMatcher
from typing import List, Tuple

from src.models.transcription.Transcript import Transcript


class SearchTermMatcher:
    def __init__(self):
        pass

    def find_sentence(self, sentence: str, transcript: Transcript) -> List[Tuple[int, int, int]]:
        indices = []
        words = transcript.full_text.split()
        sentence_words = sentence.split()

        for sw_index, search_word in enumerate(sentence_words):
            for i, word in enumerate(words):
                if word == search_word:
                    remaining_length = len(words) - i

                    if remaining_length >= len(sentence_words):
                        words_ = words[i - sw_index:i - sw_index + len(sentence_words)]
                        s = SequenceMatcher(None, words_, sentence_words)

                        if s.ratio() >= 0.4:
                            indices.append((i - sw_index, i - sw_index + len(sentence_words), s.ratio()))

        return self.deduplicate_tuples(indices)

    def deduplicate_tuples(self, tuples: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
        s = set()
        for t in tuples:
            s.add(t)
        return list(s)
