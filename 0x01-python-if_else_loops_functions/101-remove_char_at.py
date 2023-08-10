#!/usr/bin/python3

def remove_char_at(str, num):
    if num < 0:
        return (str)
    return (str[:num] + str[num+1:])
