#!/usr/bin/python3
"""A square module"""


class Square:
    """this is a square class. """
    def __init__(self, size=0):
        """This is a docstring for the init method.

        Args:
            size: The length of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """this function computes area"""
        return self.__size ** 2
