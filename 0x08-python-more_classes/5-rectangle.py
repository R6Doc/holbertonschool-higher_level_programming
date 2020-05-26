#!/usr/bin/python3
"""
Define a class Rectangle
"""


class Rectangle:
    """Representa a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize  rectangle"""
        self.width = width
        self.height = height

    def __del__(self):
        """prints when an instance has been deleted"""
        print("Bye rectangle...")

    @property
    def width(self):
        """get private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set private instance width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get private instance  height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set private instance  height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Return print string of rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """Return a string of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
