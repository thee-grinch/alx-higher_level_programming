#!/usr/bin/python3

def uniq_add(my_list=[]):
    """adds unique element of a list"""
    from functools import reduce
    addition = reduce(lambda x, y: x + y, set(my_list))
    return addition
