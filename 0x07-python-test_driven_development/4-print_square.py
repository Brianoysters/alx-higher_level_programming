#!/usr/bin/python3
""" defines a function to print a square."""


def print_square(size):
    """outputs a square with the # character.

    Args:
        size (int): outputs height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for index in range(size):
        [print("#", end="") for j in range(size)]
        print("")
