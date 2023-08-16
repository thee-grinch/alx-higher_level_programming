#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """This function searches and replaces all occurrences in an element"""
    list_cpy = list(map(lambda x: replace if x == search else x, my_list))
    return list_cpy
