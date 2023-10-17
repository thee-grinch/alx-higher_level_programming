#!/usr/bin/python3
"""this module defines a class rectangle
than inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """this is a class rectangle that inherits from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """this is a class constructor"""
        for attr, value in {
                "width": width, "height":
                height, "x": x, "y": y
                }.items():
            if not isinstance(value, int):
                raise TypeError(f"{attr} must be an integer")
        for attr, value in {"width": width, "height": height}.items():
            if value <= 0:
                raise ValueError(f"{attr} must be > 0")
        for attr, value in {"x": x, "y": y}.items():
            if value < 0:
                raise ValueError(f"{attr} must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """this is a width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """this is a width property setter"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """this is a height getter method"""
        return self.__height

    @height.setter
    def height(self, height):
        """This is a height setter method"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """this is a property getter method"""
        return self.__x

    @x.setter
    def x(self, x):
        """this is a x setter method"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """this is a property getter method"""
        return self.__y

    @y.setter
    def y(self, y):
        """this is a y setter method"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """This defines the area of a rectagle"""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def display(self):
        """this method prints the rectangle to the stdout"""
        for _ in range(self.__y):
            print()
        for i in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="") for i in range(self.__width)]
            print()

    def update(self, *args, **kwargs):
        """this saves the class instance variables to a external file"""
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            values = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, values[i], arg)

    def to_dictionary(self):
        """returns the dictionary representation of a class"""
        keys = ["id", "width", "height", "x", "y"]
        return {key: getattr(self, key) for key in keys}
