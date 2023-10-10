#!/usr/bin/python3
"""this module defines a function"""
import json


def from_json_string(my_str):
    """this function returns a python data structure"""
    return json.loads(my_str)
