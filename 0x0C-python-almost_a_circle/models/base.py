#!/usr/bin/python3
"""
Base class module
"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init Base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
