#!/usr/bin/python3
"""Defines a class Square inherited from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Betokens a square."""

    def __init__(self, size):
        """New square initialization.

        Args:
            size (int): New square size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
