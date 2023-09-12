#!/usr/bin/python3
"""Defines a function for text file insertion."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text, in a file, after each line containing a given string.

    Args:
        filename (str): Refers to the name of the file.
        search_string (str): String to search for.
        new_string (str): Refers to the string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
