#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    for i in range(len(list_of_integers)):
        if (i == 0 or list_of_integers[i] >= list_of_integers[i - 1]) and \
           (i == len(list_of_integers) - 1 or
            list_of_integers[i] >= list_of_integers[i + 1]):
            return list_of_integers[i]