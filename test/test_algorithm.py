import unittest
from palindrome.algorithms import (
    palindrome_two_pointers,

    is_palindrome_reverse,
    is_palindrome_iterators,
)


class TestPalindromeAlgorithms(unittest.TestCase):

    def setUp(self):
        self.palindromes = [
            "Anita lava la tina",
            "Se es o no se es",
            "Alli ves Sevilla",
            "A man, a plan, a canal, Panama",
            "mr owl ate my metal worm",
            "No 'x' in Nixon",
            "Able was I, I saw Elba",
            "Eva, can I see bees in a cave?",
            "12321",
            " ",
        ]

        self.non_palindromes = [
            "hello",
            "world",
            "How old are you?",
            "This is not a palindrome",
            "I am 23 years old",
            "12345",
        ]

        self.empty_string = ""
        self.single_char = "x"

    def test_palindromes(self):
        """Test that palindromes return True."""
        for func in [
            palindrome_two_pointers,
            is_palindrome_reverse,
            is_palindrome_iterators,
        ]:
            with self.subTest(algorithm=func.__name__):
                for case in self.palindromes:
                    self.assertTrue(func(case), f"Failed on palindrome: {case}")

    def test_non_palindromes(self):
        """Test that non-palindromes return False."""
        for func in [
            palindrome_two_pointers,
            is_palindrome_reverse,
            is_palindrome_iterators,
        ]:
            with self.subTest(algorithm=func.__name__):
                for case in self.non_palindromes:
                    self.assertFalse(func(case), f"Failed on non-palindrome: {case}")

    def test_empty_string(self):
        """Test that an empty string is considered a palindrome."""
        for func in [
            palindrome_two_pointers,
            is_palindrome_reverse,
            is_palindrome_iterators,
        ]:
            with self.subTest(algorithm=func.__name__):
                self.assertTrue(func(self.empty_string), "Failed on empty string")

    def test_single_character(self):
        """Test that a single character is considered a palindrome."""
        for func in [
            palindrome_two_pointers,
            is_palindrome_reverse,
            is_palindrome_iterators,
        ]:
            with self.subTest(algorithm=func.__name__):
                self.assertTrue(
                    func(self.single_char),
                    f"Failed on single character: {self.single_char}",
                )


if __name__ == "__main__":
    unittest.main()
