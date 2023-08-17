#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary."""
    while value in a_dictionary.values():
        for num, x in a_dictionary.items():
            if x == value:
                del a_dictionary[num]
                break

    return (a_dictionary)
