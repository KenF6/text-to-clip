import string
from typing import List


class TextHelper:
    def __init__(self):
        pass

    @staticmethod
    def normalize_text(text: str) -> str:
        punctuation = string.punctuation
        translator = str.maketrans('', '', punctuation)
        normalized_text = text.translate(translator).lower()
        return normalized_text

    @staticmethod
    def join_strings_with_underscores(to_join: List[str]) -> str:
        return '_'.join(to_join)

    @staticmethod
    def read_transcript(filename: str) -> str:
        with open(filename, 'r') as file:
            contents = file.read()
            return contents

    @staticmethod
    def sanitize_transcript(raw_transcript: str) -> str:
        return TextHelper.make_word_list_unique(TextHelper.turn_text_into_plain_word_list(raw_transcript))

    @staticmethod
    def turn_text_into_plain_word_list(text: str) -> List[str]:
        words = text.split()

        lower_case_words = [word.lower() for word in words]
        plain_words = TextHelper.remove_all_punctuation(lower_case_words)

        return plain_words

    @staticmethod
    def remove_all_punctuation(word_list: List[str]) -> List[str]:
        plain_words = []
        for word in word_list:
            plain_words.append(word.translate(str.maketrans('', '', string.punctuation)))
        return plain_words

    @staticmethod
    def make_word_list_unique(word_list: List[str]) -> List[str]:
        return list(set(word_list))
