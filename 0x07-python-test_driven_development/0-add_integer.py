#!/usr/bin/python3
# 0-add_integer.py
"""Defines function integer addition."""


def add_integer(a, b=98):
    """Returns integer addition of a and b.

    Before addition is performed, float arguments are typecasted to ints.

    Raises:
        TypeError: When either of a or b is a non-float and non-integer.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
