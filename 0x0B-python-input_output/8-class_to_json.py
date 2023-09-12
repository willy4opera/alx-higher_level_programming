#!/usr/bin/python3

"""Here, we defined the Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    result = obj.__dict__
    return result
