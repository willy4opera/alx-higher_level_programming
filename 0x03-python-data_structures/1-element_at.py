#!/usr/bin/python3

# Function retrieves an element from a List.

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return
    return my_list[idx]
