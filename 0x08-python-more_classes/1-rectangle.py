#!/usr/bin/python3

""" a square module"""

class Rectangle:
    """this defines a rectangle class"""
    def __init__(self, width=0, height=0):
        """This is a class constructor"""
        if isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if isinstance(height, int):
            raise TypeError("height must be an integer")
        if heigth < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
    
