#!/usr/bin/python3
"""This function Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds the peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    d_low = 0
    d_high = len(list_of_integers)
    d_mid = ((d_high - d_low) // 2) + d_low
    d_mid = int(d_mid)
    if d_high == 1:
        return list_of_integers[0]
    if d_high == 2:
        return max(list_of_integers)
    if list_of_integers[d_mid] >= list_of_integers[d_mid - 1] and\
            list_of_integers[d_mid] >= list_of_integers[d_mid + 1]:
        return list_of_integers[d_mid]
    if d_mid > 0 and list_of_integers[d_mid] < list_of_integers[d_mid + 1]:
        return find_peak(list_of_integers[d_mid:])
    if d_mid > 0 and list_of_integers[d_mid] < list_of_integers[d_mid - 1]:
        return find_peak(list_of_integers[:d_mid])
