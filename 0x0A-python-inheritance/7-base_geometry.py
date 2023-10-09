#!/usr/bin/python3
"""this is a module with a class"""


class BaseGeometry():
    """this is a class"""
    def area(Self):
        """this is a method"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """this is another method"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

