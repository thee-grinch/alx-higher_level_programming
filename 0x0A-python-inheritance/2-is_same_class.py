#!/usr/bin/python3
"""This module atempts to find if a module
is the same instance"""


def is_same_class(obj, a_class):
    """return true if they are of the same class"""
    return isinstance(obj, a_class)
