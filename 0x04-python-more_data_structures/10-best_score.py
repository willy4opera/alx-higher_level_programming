#!/usr/bin/python3


def best_score(a_dictionary):
    """
    A function that returns a key with the biggest integer value.
    """
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        score = 0
        lst = ""
        for num in my_list:
            if a_dictionary[num] > score:
                score = a_dictionary[num]
                lst = num
        return lst
