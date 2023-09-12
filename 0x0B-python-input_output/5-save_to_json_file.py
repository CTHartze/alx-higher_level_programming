#!/usr/bin/python3
"""Defines a function for JSON file-writing."""
import json


def save_to_json_file(my_obj, filename):
    """Writes JSON representation of object to a text file."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
