#!/usr/bin/python3



def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    lst = list(a_dictionary.keys())[0]
    bda = a_dictionary[lst ]
    for x, y in a_dictionary.items():
        if y > bda:
            bda = y
            lst  = x
    return (lst)
