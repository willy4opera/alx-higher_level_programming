#!/usr/bin/python3
# Removes character C and c

def no_c(my_string):
    strn_cpy = [n for n in my_string if n != 'c' or n != 'C']
    return ("".join(strn_cpy))
