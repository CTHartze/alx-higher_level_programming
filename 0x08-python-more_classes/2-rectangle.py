#!/usr/bin/python3
"""Betokens Rectangle class."""


class Rectangle:
    """Betokens a rectangle."""

    def __init__(self, width=0, height=0):
        """New Rectangle initializer.

        Args:
            width (int): Refers to new rectangles width.
            height (int): New rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets/sets rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets/sets rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns rectangles area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns rectangles perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
