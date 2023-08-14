#!/usr/bin/python3

# Removes character C and c

def no_c(my_string):
    strn_cp = my_string.translate({ord('c'): None})
    strn_cp = strn_cp.translate({ord('C'): None})
    return strn_cp
