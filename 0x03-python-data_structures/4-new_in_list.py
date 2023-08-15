#!/usr/bin/python3

# Print New in List.

def new_in_list(my_list, idx, element):

    if (idx < 0) or (idx > (len(my_list)-1)):
        return my_list

    d_copy = [num for num in my_list]
    d_copy[idx] = element
    return d_copy
