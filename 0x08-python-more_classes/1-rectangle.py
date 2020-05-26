#!/usr/bin/python3
"""
Define a class Rectangle
"""


class Rectangle:
    """represent a rectangle"""
    def __init__(self, width=0, height=0):
        """Initial rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """get the private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the private instance width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the private instance height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
