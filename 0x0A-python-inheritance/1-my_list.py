#!/usr/bin/python3
"""
contain MyList class
"""


class MyList(list):
    """subclass list"""
    def __init__(self):
        """initialize object"""
        super().__init__()

    def print_sorted(self):
        """print the sorted list"""
        print(sorted(self))
