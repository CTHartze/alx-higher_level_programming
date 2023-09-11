#!/usr/bin/python3
"""Defines class and function for inherited class-checking."""


def is_kind_of_class(obj, a_class):
    """Checks if object is an instance or a class inherited instance.

    Args:
        obj (any): Refers to object to check.
        a_class (type): Class to match obj type to.
    Returns:
        If obj is an instance or a_class inherited instance - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
