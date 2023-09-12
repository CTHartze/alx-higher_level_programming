#!/usr/bin/python3
"""Defines a function for file-writing."""


def write_file(filename="", text=""):
    """Writes string to a UTF8 text file.

    Args:
        filename (str): Name of the file to write.
        text (str): Refers to the text to write.
    Returns:
        Amount of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
