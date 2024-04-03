from favourite_words.input.get_words import get_entries_from_console
from favourite_words.output.save_words import save_words


def add_words():
    entries = get_entries_from_console()
    save_words(entries)


if __name__ == "__main__":
    add_words()
