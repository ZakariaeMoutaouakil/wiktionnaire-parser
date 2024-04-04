from typing import List

from dictionnaire.dictionary import dictionary
from favourite_words.add_words import add_words
from favourite_words.vocab_parser.parse_vocab import read_vocab_file
from util.dict_to_json import pretty_json


def get_all_definitions(words: List[str]):
    return [dictionary(word) for word in words]


if __name__ == '__main__':
    add_words()
    content = read_vocab_file()  # Reads the content of "vocab.txt"
    print(pretty_json(get_all_definitions(content)))
