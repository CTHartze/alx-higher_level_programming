#!/usr/bin/python3
"""Defines MyList for inherited list class."""


class MyList(list):
    """Implements printing sorted for built-in list class."""

    def print_sorted(self):
        """Prints list sorted in ascending order."""
        print(sorted(self))
