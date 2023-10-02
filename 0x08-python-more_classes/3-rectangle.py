#!/usr/bin/python3
"""This module creates a class rectangle"""


class Rectangle:
    """This module creates the rectangle class and its methods"""
    def __init__(self, width=0, height=0):
        """this is for initializing the object"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """This is a getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This is a setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """This computes the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """this computes the perimeter of the triangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Formated printing method"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            [rect.append("#") for _ in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))


