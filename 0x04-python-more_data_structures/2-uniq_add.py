#!/usr/bin/python3

def uniq_add(my_list=[]):
    """adds unique element of a list"""
    addition = 0
    unique_set = set(my_list)
    for num in unique_set:
        addition += num
    return addition
