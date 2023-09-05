#!/usr/bin/python3

"""Here, we defines a locked class."""


class LockedClass:
    """
    This class Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
