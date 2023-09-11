#!/usr/bin/python3
"""Defines lookup function for object attribute."""


def lookup(obj):
    """Returns list of object attributes available."""
    return (dir(obj))
