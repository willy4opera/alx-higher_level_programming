#!/usr/bin/python3

#  A function that prints a dictionary by ordered keys.

def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(n, a_dictionary[n])) for n in sorted(a_dictionary)]
