#!/usr/bin/python3

"""A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        __init__(self, width=0, height=0):
            Initializes a rectangle with the given width and height.

        width (property):
            Gets the width of the rectangle.

        height (property):
            Gets the height of the rectangle.

        width (setter):
            Sets the width of the rectangle. Must be an integer >= 0.

        height (setter):
            Sets the height of the rectangle. Must be an integer >= 0.
    """


class Rectangle:
    """this defines a rectangle class"""
    def __init__(self, width=0, height=0):
        """This is a class constructor
        Args:
        width(int): the width of a rectangle
        height(int): the height of a triangle

        Raises:
        TypeError: If the width or height is not an int
        ValueError: if Width or height is less than 0
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def height(self):
        """this is a getter method for height"""

        return self.__height

    @property
    def width(self):
        """This is a getter method for width"""

        return self.__width

    @width.setter
    def width(self, value):
        """This method sets the width
        Args:
            value(int): the value to be set
        RAises:
            TypeError: if the value is not int
            ValueError: if the value is negative
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """This method sets the height
        Args:
            value(int): the value to be set
        RAises:
            TypeError: if the value is not int

          ValueError: if the value is negative
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """This is a format for printing"""
        if self.__height == 0 or self.__width == 0:
            return ""
        shape = ""
        for _ in range(self.__height):
            shape += "#" * self.__width + "\n"
        return shape

    def __repr__(self):
        """This is a format for printing"""
        if self.__height == 0 or self.__width == 0:
            return ""
        return f"Rectangle({self.__width}, {self.__height})"
