#!/usr/bin/python3
"""Defines a Rectangle class inherited from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Uses BaseGeometry to represent a rectangle."""

    def __init__(self, width, height):
        """New Rectangle initialization.

        Args:
            width (int): New Rectangle width.
            height (int): New Rectangle height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
