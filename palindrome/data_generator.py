import random
import string


def generate_random_string(size, ensure_palindrome=False):

    half = "".join(random.choices(string.ascii_lowercase, k=size // 2))

    if ensure_palindrome:
        return half + (
            half[::-1]
            if size % 2 == 0
            else random.choice(string.ascii_lowercase) + half[::-1]
        )
    else:
        return "".join(random.choices(string.ascii_lowercase, k=size))


def get_random_strings(size, samples, ensure_palindrome=False):

    return [
        generate_random_string(size, ensure_palindrome=ensure_palindrome)
        for _ in range(samples)
    ]
