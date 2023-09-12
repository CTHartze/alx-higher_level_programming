#!/usr/bin/python3
"""Defines a function for string-to-JSON."""
import json


def to_json_string(my_obj):
    """Returns a string object in JSON representation."""
    return json.dumps(my_obj)
