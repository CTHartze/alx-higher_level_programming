#!/usr/bin/python3
# 4-print_square.py
"""Defines function for square-printing."""


def print_square(size):
    """Prints square with # character.

    Args:
        size (int): The width/height of the square.
    Raises:
        TypeError: When size is not an integer.
        ValueError: When size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
