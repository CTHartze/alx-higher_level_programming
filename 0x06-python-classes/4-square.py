#!/usr/bin/python3
"""Defines class square according to 3-square.py."""

class Square:
    """Square representative."""

    def __init__(self, size=0):
        """
        New square initializer.

        Args:
            size (int): Refers to size of new square.
        """
        self.size = size

    @property
    def size(self):
        """Gets/Sets current size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the squares current area."""
        return (self.__size * self.__size)
