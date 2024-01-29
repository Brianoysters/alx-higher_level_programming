#!/usr/bin/python3
"""This function defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): Text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    _char = 0
    while _char < len(text) and text[_char] == ' ':
        _char += 1

    while _char < len(text):
        print(text[_char], end="")
        if text[_char] == "\n" or text[_char] in ".?:":
            if text[_char] in ".?:":
                print("\n")
            _char += 1
            while _char < len(text) and text[_char] == ' ':
                _char += 1
            continue
        _char += 1
