"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
### git comment
"""
import pytest


def no_duplicates(a_string):
    sortedString = ""
    for char in a_string:
        if len(sortedString) == 0:
            sortedString = char
        else:
            for i in range(len(sortedString)):
                if sortedString[i] == char:
                    break
                elif sortedString[i] > char:
                    sortedString = sortedString[0: i] + char + sortedString[i: len(sortedString)]
                    break
                elif i == len(sortedString) - 1:
                    sortedString = sortedString + char
                    break
    return sortedString
    pass


def reversed_words(a_string):
    return list(reversed(a_string.split(sep=" ")))
    pass


def four_char_strings(a_string):
    chunks, chunk_size = len(a_string), 4
    return [a_string[i:i + chunk_size] for i in range(0, chunks, chunk_size)]
    pass


def test_no_duplicates():
    s = 'monty pythons flying circus'
    print("print of no_duplicates ", no_duplicates(s))
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    print("print of reversed_words ", reversed_words(s))
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s = 'monty pythons flying circus'
    print("print of four_char_strings ", four_char_strings(s))
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']


def main():
    test_no_duplicates()
    test_reversed_words()
    test_four_char_strings()
    return pytest.main(__file__)


if __name__ == '__main__':
    main()
