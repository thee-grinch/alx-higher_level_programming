#!/usr/bin/python3
"""this module defines a class"""


def class_to_json(obj):
    """returns a dictionary representation"""
    return obj.__dict__
