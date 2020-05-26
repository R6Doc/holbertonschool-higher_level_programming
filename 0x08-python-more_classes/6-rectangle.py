#!/usr/bin/python3
"""
Define a class Rectangle
"""


class Rectangle:
    """Representa a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """print a string when an instance has been deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """get for the private instance width"""
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

    def area(self):
        """retur area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """retur perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns print string of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """return a string of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
