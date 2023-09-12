#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a function for JSON-to-object."""
import json


def from_json_string(my_str):
    """Returns a JSON string in Python object representation."""
    return json.loads(my_str)
