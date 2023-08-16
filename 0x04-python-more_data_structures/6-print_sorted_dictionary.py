#!/usr/bin/python3

#  A function that prints a dictionary by ordered keys

def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(num, a_dictionary[num])) for num in sorted(a_dictionary)]
