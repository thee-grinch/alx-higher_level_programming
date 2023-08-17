#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for person in a_dictionary:
        new_dict[person] *= 2
    return new_dict
