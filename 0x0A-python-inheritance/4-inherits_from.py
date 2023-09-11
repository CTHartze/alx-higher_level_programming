#!/usr/bin/python3
"""Defines function for inherited class-checking."""


def inherits_from(obj, a_class):
    """Checks if object is a class inherited instance.

    Args:
        obj (any): Refers to object to check.
        a_class (type): Class to match the obj type to.
    Returns:
        If obj is an a_class inherited instance - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
