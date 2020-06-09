#!/usr/bin/python3
"""
Base class module
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON string of a list of dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
