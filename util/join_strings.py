from typing import List


def concatenate_with_pipe(strings: List[str], pipe: str = "|") -> str:
    return pipe.join(strings)


if __name__ == "__main__":
    # Example usage:
    list_of_strings = ["apple", "banana", "orange"]
    result = concatenate_with_pipe(strings=list_of_strings)
    print(result)  # Output: apple|banana|orange
