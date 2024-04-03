import re


def extract_number_from_string(input_string: str) -> int | None:
    """
    Extracts a number from a string using regular expressions.

    Args:
        input_string (str): The input string from which to extract the number.

    Returns:
        int or None: The extracted number if found, otherwise None.
    """
    # Regular expression to match any number
    number_pattern = r'\d+'

    # Extract the number from the string using re.findall()
    numbers = re.findall(number_pattern, input_string)

    # If there are multiple numbers, you can choose the desired one, for instance, the first one
    if numbers:
        extracted_number = int(numbers[0])
        return extracted_number

    return None
