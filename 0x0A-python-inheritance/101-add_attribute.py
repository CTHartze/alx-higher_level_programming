#!/usr/bin/python3
"""Defines a function that adds object attributes."""


def add_attribute(obj, att, value):
    """If possible, adds new object attribute.

    Args:
        obj (any): Object to add an attribute to.
        att (str): Refers to attribute to add to obj.
        value (any): Refers to value of att.
    Raises:
        TypeError: If unable to add attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
