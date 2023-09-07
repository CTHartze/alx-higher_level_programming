#!/usr/bin/python3
# 3-say_my_name.py
"""Defines function for name-printing."""


def say_my_name(first_name, last_name=""):
    """Prints name.

    Args:
        first_name (str): Refers to name to print.
        last_name (str): Refers to last name to print.
    Raises:
        TypeError: When either first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
