import unittest

from util.extract_number import extract_number_from_string


class TestExtractNumberFromString(unittest.TestCase):

    def test_extract_number_from_string(self):
        # Test case where a number is present in the string
        input_string = "This is a test string with the number 123."
        expected_number = 123
        self.assertEqual(extract_number_from_string(input_string), expected_number)

        # Test case where multiple numbers are present, the method should return the first one
        input_string = "This string contains multiple numbers like 456 and 789."
        expected_number = 456
        self.assertEqual(extract_number_from_string(input_string), expected_number)

        # Test case where no number is present in the string
        input_string = "This string does not contain any number."
        self.assertIsNone(extract_number_from_string(input_string))


if __name__ == '__main__':
    unittest.main()
