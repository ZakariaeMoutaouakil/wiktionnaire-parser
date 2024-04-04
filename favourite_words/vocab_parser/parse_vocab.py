from typing import List


def validate_vocab_file(file_name: str = "vocab.txt"):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            for line in lines:
                if not line.strip():  # Skip empty lines
                    continue
                words = line.split()
                if len(words) != 1:
                    print(f"Error: Line '{line.strip()}' in file '{file_name}' contains more than one word.")
                    return False
        print(f"File '{file_name}' content is valid.")
        return True
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return False


def read_vocab_file(file_name: str = "vocab.txt") -> List[str]:
    if not validate_vocab_file(file_name):
        print(f"Error: File '{file_name}' is invalid.")
        return []

    try:
        with open(file_name, "r") as file:
            words = [line.strip() for line in file if line.strip()]
        return list(set(words))
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return []


if __name__ == "__main__":
    # Example usage:
    print(validate_vocab_file())  # Validates the content of "vocab.txt"

    content = read_vocab_file()  # Reads the content of "vocab.txt"
    print(content)
