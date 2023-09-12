#!/usr/bin/python3

"""Here, we Add all arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        d_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        d_items = []
    d_items.extend(sys.argv[1:])
    save_to_json_file(d_items, "add_item.json")
