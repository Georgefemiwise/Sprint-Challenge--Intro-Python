"""
Challenge: Palindrome Checker

Write a Python function that checks whether a given word or phrase is a palindrome. 
A palindrome is a word, phrase, number, or other sequences of characters that reads the same 
forward and backward (ignoring spaces, punctuation, and capitalization).

For example:

    "radar" is a palindrome.
    "A man, a plan, a canal: Panama" is a palindrome.
    "python" is not a palindrome.

Your function should return True if the input is a palindrome and False otherwise. 
Make sure to handle different cases and ignore non-alphanumeric characters.

"""

# Here's a function signature to get you started:


def is_palindrome(s: str):
    s = s.translate(str.maketrans("", "", ",: "))
    return s.lower() == s[::-1].lower()


# # Test cases
print(is_palindrome("radar"))  # Should print True
print(is_palindrome("A man, a plan, a canal: Panama"))  # Should print True
print(is_palindrome("python"))  # Should print False
