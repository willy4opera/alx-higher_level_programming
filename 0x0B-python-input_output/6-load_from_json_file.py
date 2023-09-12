#!/usr/bin/python3

"""Here, we defined the JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as f:
        result = json.load(f)
        return result
