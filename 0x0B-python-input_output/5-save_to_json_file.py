#!/usr/bin/python3

"""Here, we defined the JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Here, we write an object to a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
