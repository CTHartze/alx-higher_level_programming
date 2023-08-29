#!/usr/bin/python3
"""Defines class square according to 1-square.py."""


class Square:
    """square representative."""

    def __init__(self, size=0):
        """
        New square iniatilizer.

        Args:
            size (int): Refers to size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
