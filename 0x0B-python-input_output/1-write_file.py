#!/usr/bin/python3

"""Here, we defines a file-writing function."""


def write_file(filename="", text=""):
    """Here, we write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        result = f.write(text)
        return result
