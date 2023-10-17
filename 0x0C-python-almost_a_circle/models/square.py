#!/usr/bin/python3
from models.rectangle import Rectangle
"""this module defines a class
square that import from rectangle"""


class Square(Rectangle):
    """this is a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """This is a class initializer that calls the super method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """this is a class str method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """this is a size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """this is a size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """this is an update method for self"""
        if len(args) == 0:
            for item, value in kwargs.items():
                setattr(self, item, value)
        else:
            values = ["id", "size", "x", "y"]
            for idx, value in enumerate(args):
                setattr(self, values[idx], value)

    def to_dictionary(self):
        """this returns the dictionary representation"""
        keys = ["id", "size", "x", "y"]
        return {key: getattr(self, key) for key in keys}
