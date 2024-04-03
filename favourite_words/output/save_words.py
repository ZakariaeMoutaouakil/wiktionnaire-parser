from typing import List


def append_to_vocab_file(data: str, file_name="vocab.txt"):
    try:
        with open(file_name, "a") as file:
            file.write(data + "\n")
    except Exception as e:
        print(f"Error appending data to '{file_name}': {e}")


def save_words(strings: List[str], file_name="vocab.txt"):
    for string in strings:
        append_to_vocab_file(string, file_name)


if __name__ == "__main__":
    # Example usage:
    list_of_strings = ["apple", "fruit", "red"]
    save_words(strings=list_of_strings)
