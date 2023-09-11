#!/usr/bin/python3
""" Here we defined an object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    result = dir(obj)
    return (result )
