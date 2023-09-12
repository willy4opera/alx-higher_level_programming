#!/usr/bin/python3

"""Here, we defined the JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    result = json.loads(my_str)
    return result
