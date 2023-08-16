#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(num, a_dictionary[num])) for num in sorted(a_dictionary)]
