#!/usr/bin/python3

# adds all unique integers in a list 

def uniq_add(my_list=[]):
    result = 0
    for num in set(my_list):
        result += num
    return result
