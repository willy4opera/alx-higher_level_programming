#!/usr/bin/python3

# Adds all unique integers in a list 

def uniq_add(my_list=[]):
    result = 0
    for a in set(my_list):
        result += a
    return result
