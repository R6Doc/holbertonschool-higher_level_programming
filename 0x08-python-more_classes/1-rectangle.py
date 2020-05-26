#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        """Initialize triangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """get private var"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the private var width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the private var height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the private attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
