#!/usr/bin/python3
"""Defines function for class-checking."""


def is_same_class(obj, a_class):
    """Checks if object is an exact instance of a given class.

    Args:
        obj (any): Refers to object to check.
        a_class (type): Class to match obj type to.
    Returns:
        If obj is an exact instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
