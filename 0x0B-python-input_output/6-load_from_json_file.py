#!/usr/bin/python3
"""this module defines a function"""
import json


def load_from_json_file(filename):
    """this module reads a json object"""
    with open(filename, "r") as file:
        return json.load(file)
