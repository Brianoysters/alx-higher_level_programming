#!/usr/bin/python3
"""Function defines  a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Width of the new rectangle.
            height (int): Height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """outputs the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width is an integer")
        if value < 0:
            raise ValueError("width >= 0")
        self.__width = value

    @property
    def height(self):
        """outputs the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height is an integer")
        if value < 0:
            raise ValueError("height >= 0")
        self.__height = value
