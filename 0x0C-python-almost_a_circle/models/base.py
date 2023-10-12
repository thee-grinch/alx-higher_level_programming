#!/usr/bin/python3
"""This module defines a base class"""


class Base():
    """This is a base class for managing id
    attributes for future classes"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        """This is a class constructor
        with public instance attr id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
