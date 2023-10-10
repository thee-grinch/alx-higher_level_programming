#!/usr/bin/python3
"""this module defines a class"""


class Student:
    """this is a student class"""
    def __init__(self, first_name, last_name, age):
        """this is a class constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary representation of a string"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
