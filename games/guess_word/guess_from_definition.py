from random import choice

from favourite_words.vocab_parser.parse_vocab import read_vocab_file
from txt_to_dictionary.get_all_definitions import get_all_definitions


def guess_from_definition():
    words = read_vocab_file()
    all_defs = get_all_definitions(words=words)
    word = choice(all_defs)
    definitions = next(iter(word.values()), None)
    word_sense = choice(definitions)

    print("Devine le mot: " + word_sense['définition'])
    print("Parmi les mots suivants: " + str(words))

    answer = input()
    true_answer = next(iter(word.keys()), None)

    if answer.lower() == true_answer:
        print("Bonne réponse!")

        try:
            exemples = word_sense['exemples']
            print("Voici des exemples: ")
            for exemple in exemples:
                print(exemple)
        except KeyError:
            pass

    else:
        print("Le vrai mot est: \"" + true_answer + "\".")


if __name__ == '__main__':
    while True:
        guess_from_definition()
