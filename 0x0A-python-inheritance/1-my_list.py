#!/usr/bin/python3
"""this instance derives a class my list"""


class MyList(list):
    """is a class under my list"""
    def print_sorted(self):
        """prints a list which is sorted"""
        print(sorted(self))
