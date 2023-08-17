#!/usr/bin/python3

# A function that returns a new dictionary with all values multiplied by 2

def multiply_by_2(a_dictionary):
    return ({n: a_dictionary[n] * 2 for n in a_dictionary})
