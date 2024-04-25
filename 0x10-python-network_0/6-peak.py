#!/usr/bin/python3
"""Defines a peak-finding algorithm."""

def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    min_ = len(list_of_integers)
    if min_ == 1:
        return list_of_integers[0]
    elif min_ == 2:
        return max(list_of_integers)

    mid = int(min_ / 2)
    max_ = list_of_integers[mid]
    if max_ > list_of_integers[mid - 1] and max_ > list_of_integers[mid + 1]:
        return max_
    elif max_ < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])

