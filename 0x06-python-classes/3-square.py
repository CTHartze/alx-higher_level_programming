#!/usr/bin/python3
"""Defines class square according to 2-square.py."""

class Square:
    """Square representative."""

    def __init__(self, size=0):
        """
        New square iniatilizer.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
