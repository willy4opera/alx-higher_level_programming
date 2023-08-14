#!/usr/bin/python3


def no_c(my_string):
    strn_cpy = [num for num in my_string if num != 'c' or num != 'C']
    data = "".join(strn_cpy)
    return (data)
