#!/usr/bin/python3
"""Defines a function for file-appending."""


def append_write(filename="", text=""):
    """String is appended to the end of a UTF8 text file.

    Args:
        filename (str): Name of the file to append to.
        text (str): Refers to the string to append.
    Returns:
        Amount of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
