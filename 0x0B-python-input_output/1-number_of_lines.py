#!/usr/bin/python3
"""
Contain number_of_lines function
"""


def number_of_lines(filename=""):
    """returnnumber of lines of a text file"""
    with open(filename, 'r', encoding='utf8') as f:
        i = 0
        for line in f:
            i += 1
        return i
