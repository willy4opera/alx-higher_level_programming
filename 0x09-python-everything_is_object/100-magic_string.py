#!/usr/bin/python3
def magic_string():
    mgc_strng.n = getattr(mgc_strng, 'n', 0) + 1
    return ("BestSchool, " * (mgc_strng.n - 1) + "BestSchool")
