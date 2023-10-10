#!/usr/bin/python3
"""this module defines a class"""


class Student:
    """this is a student class"""
    def __init__(self, first_name, last_name, age):
        """this is a class constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary representation of a string"""
        return self.__dict__
