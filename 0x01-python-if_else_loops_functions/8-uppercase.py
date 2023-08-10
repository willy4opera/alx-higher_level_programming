#!/usr/bin/python3

def uppercase(str):
    """Print a string in uppercase."""
    for lett in str:
        if ord(lett) >= 97 and ord(lett) <= 122:
            lett = chr(ord(lett) - 32)
        print("{}".format(lett), end="")
    print("")
