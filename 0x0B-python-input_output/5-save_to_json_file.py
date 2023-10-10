#!/usr/bin/python3
"""this module defines a function"""
import json


def save_to_json_file(my_obj, filename):
    """this function saves an object to a file
        using json representation"""
    with open(filename, "w") as j_file:
        json.dump(my_obj, j_file)
