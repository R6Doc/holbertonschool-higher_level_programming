#!/usr/bin/python3
"""
Readfile function
"""


def read_file(filename=""):
    """ Reads a file content with with statement"""
    with open("my_file_0.txt", encoding="UTF8") as myfile:
        print(myfile.read())
