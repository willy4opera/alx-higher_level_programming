#!/usr/bin/python3



def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    retlist = list(a_dictionary.keys())[0]
    bdata = a_dictionary[retlist ]
    for x, y in a_dictionary.items():
        if y > bdata:
            bdata = y
            retlist  = x
    return (retlist)
