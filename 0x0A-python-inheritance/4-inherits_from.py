#!/usr/bin/python3
"""this module checks a subclass"""


def inherits_from(obj, a_class):
    """checks whether is a subclass"""
    return issubclass(type(obj), object) and not type(obj) == a_class
