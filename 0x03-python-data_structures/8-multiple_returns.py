#!/usr/bin/python3

def multiple_returns(sentence):
    dev_tuple = ()
    if len(sentence) == 0:
        dev_tuple = 0, "None"
    else:
        dev_tuple = len(sentence), sentence[0]
    return dev_tuple
