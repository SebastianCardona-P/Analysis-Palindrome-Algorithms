import unittest
from palindrome.data_generator import generate_random_string, get_random_strings

class TestDataGenerator(unittest.TestCase):

    def test_generate_random_string_creates_correct_length(self):
        result = generate_random_string(10)
        self.assertEqual(len(result), 10)

    def test_generate_random_string_creates_palindrome_even_length(self):
        result = generate_random_string(6, ensure_palindrome=True)
        self.assertEqual(result, result[::-1])

    def test_generate_random_string_creates_palindrome_odd_length(self):
        result = generate_random_string(7, ensure_palindrome=True)
        self.assertEqual(result, result[:3] + result[3] + result[2::-1])

    def test_generate_random_string_creates_non_palindrome(self):
        result = generate_random_string(10, ensure_palindrome=False)
        self.assertNotEqual(result, result[::-1])

    def test_get_random_strings_creates_correct_number_of_strings(self):
        result = get_random_strings(10, 5)
        self.assertEqual(len(result), 5)

    def test_get_random_strings_creates_palindromes(self):
        result = get_random_strings(6, 3, ensure_palindrome=True)
        for s in result:
            self.assertEqual(s, s[::-1])

    def test_get_random_strings_creates_non_palindromes(self):
        result = get_random_strings(10, 3, ensure_palindrome=False)
        for s in result:
            self.assertNotEqual(s, s[::-1])

if __name__ == '__main__':
    unittest.main()