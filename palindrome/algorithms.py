def palindrome_two_pointers(s):  # O(n)
    s = "".join(c.lower() for c in s if c.isalnum())  # O(n)
    left, right = 0, len(s) - 1  # O(1)

    while left < right:  # O(n/2)
        if s[left] != s[right]:  # Compare characters from left and right
            return False
        left += 1
        right -= 1

    return True


# O(palindrome_two_pointers) = O(n) + O(1) + O(n/2) + O(1) = O(n)


def is_palindrome_reverse(s):
    s = "".join(c.lower() for c in s if c.isalnum())  # O(n)
    reversed_s = s[::-1]  # O(n)
    return s == reversed_s  # O(1)


# O(is_palindrome_reverse) = O(n) + O(n) + O(1) = O(n)


def is_palindrome_iterators(s):
    s = "".join(c.lower() for c in s if c.isalnum())  # O(n)
    return all(left == right for left, right in zip(s, reversed(s)))  # O(n)


# O(is_palindrome_iterators) = O(n) + O(n) = O(n)


def is_palindrome_recursive(s):
    s = "".join(c.lower() for c in s if c.isalnum())  # O(n)

    def check(s, left, right):
        if left >= right:  # O(1)
            return True
        if s[left] != s[right]:  # O(1)
            return False
        return check(s, left + 1, right - 1)  # O(n)

    return check(s, 0, len(s) - 1)  # O(n)


# O(is_palindrome_recursive) = O(n) + O(1) + O(1) + O(n) = O(n)
