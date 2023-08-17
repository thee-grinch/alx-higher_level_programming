#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    power = lambda x: x * 2
    for person in a_dictionary:
        new_dict[person] = power(new_dict.get(person))
    return new_dict
