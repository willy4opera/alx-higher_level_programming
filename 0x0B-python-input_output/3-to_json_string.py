#!/usr/bin/python3

"""Here, we defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    result = json.dumps(my_obj)
    return result
