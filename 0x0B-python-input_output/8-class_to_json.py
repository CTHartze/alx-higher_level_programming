#!/usr/bin/python3
"""Defines a function for Python class-to-JSON."""


def class_to_json(obj):
    """Returns a simple data structure in dictionary representation."""
    return obj.__dict__
