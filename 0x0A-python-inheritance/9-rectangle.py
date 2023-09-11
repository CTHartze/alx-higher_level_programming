#!/usr/bin/python3
"""Defines a class Rectangle inherited from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Betokens rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """New Rectangle initialization.

        Args:
            width (int): New Rectangle width.
            height (int): New Rectangle height.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the Rectangle area."""
        return self.__width * self.__height

    def __str__(self):
        """Returns print() and str() Rectangle representation."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
