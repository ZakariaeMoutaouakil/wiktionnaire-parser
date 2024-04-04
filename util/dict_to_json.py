import json
from typing import Dict, List, Union


def pretty_json(dictionary: Union[List[Dict], Dict]):
    """
    Print a dictionary as a pretty JSON string with indentation.

    Args:
        dictionary (Dict): The dictionary to print as pretty JSON.

    Returns:
        None
    """
    # Convert dictionary to pretty JSON string with indentation
    pretty_json_string = json.dumps(dictionary, indent=4, ensure_ascii=False)

    # Print pretty JSON string
    return pretty_json_string


if __name__ == "__main__":
    # Sample array of dictionaries
    array_of_dicts = [
        {'name': 'John', 'age': 30, 'city': 'New York'},
        {'name': 'Alice', 'age': 25, 'city': 'Los Angeles'}
    ]

    # Call the function with the sample dictionary
    print(pretty_json(array_of_dicts))
