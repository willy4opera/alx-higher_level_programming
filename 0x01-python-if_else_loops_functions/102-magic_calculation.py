#!/usr/bin/python3

def magic_calculation(xx, yy, zz):
    if xx < yy:
        return (zz)
    if zz > yy:
        return (xx + yy)
    return (xx*yy - zz)
