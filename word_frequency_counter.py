"""Certainly! Here's another Python challenge for you:

**Challenge: Word Frequency Counter**

Write a Python function that takes a string as input and returns a dictionary containing the frequency of each word in the string. Ignore case and consider only alphanumeric characters.

For example:

Your function should convert the text to lowercase, remove non-alphanumeric characters, and then count the frequency of each word.

Feel free to use any data structure or method you find suitable for this task. Good luck!"""


def word_frequency_counter(text: str):
    frq: dict = {}
    text = text.lower()
    text = text.translate(str.maketrans("", "", ",!"))

    for i in text.split(" "):
        frq[i] = text.count(i)

    return frq


# Test case
text = "Hello world, hello Python! World of Python is awesome."
result = word_frequency_counter(text)
print(result)

# Should print: {'hello': 2, 'world': 2, 'python': 2, 'of': 1, 'is': 1, 'awesome': 1}
import collections


def word_frequency_counter(text: str):
    text = text.lower()
    text = text.translate(str.maketrans("", "", ",!"))

    list_text = text.split(" ")
    count_text = collections.Counter(list_text)

    return dict(count_text)


# Test case
text = "Hello world, hello Python! World of Python is awesome."
result = word_frequency_counter(text)
print(result)
