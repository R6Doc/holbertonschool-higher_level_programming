#!/usr/bin/python3
"""
Square Class module
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init Square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Gets size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets size value"""
        self.width = value
        self.height = value

    def __str__(self):
        """informal string of the square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    def update(self, *args, **kwargs):
        """Update Attributes"""
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.y = j
                elif i == 3:
                    self.x = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.y = kwargs["y"]
            if "y" in kwargs:
                self.x = kwargs["x"]

    def to_dictionary(self):
        """dictionary of a Square"""
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d
