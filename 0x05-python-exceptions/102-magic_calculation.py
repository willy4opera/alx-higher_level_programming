#!/usr/bin/python3


def magic_calculation(a, b):
    res = 0
    for num in range(1, 3):
        try:
            if num > a:
                raise Exception('Too far')
            else:
                res += a ** b / num
        except:
            res = b + a
            break
    return (res)
