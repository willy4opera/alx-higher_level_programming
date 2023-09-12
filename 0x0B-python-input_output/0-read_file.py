#!/usr/bin/python3

"""Here, we Defined the text file-reading function here."""


def read_file(filename=""):
    """ Here, we printed the contents of a UTF8 text file to stdout. """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
