#!/usr/bin/python3
"""this module checks a subclass"""


def inherits_from(obj, a_class):
    """checks whether is a subclass"""
return isinstance(obj, object) and issubclass(obj.__class__, a_class)
