#!/usr/bin/python3
"""Function helps in pinting name."""


def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): The first name.
        last_name (str): The last name.
    Raises:
        TypeError: If neither are strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be string")
    print("My name is {} {}".format(first_name, last_name))
