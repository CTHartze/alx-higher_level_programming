#!/usr/bin/python3
"""Defines a function for JSON file-reading."""
import json


def load_from_json_file(filename):
    """A python object created from a JSON file."""
    with open(filename) as f:
        return json.load(f)
