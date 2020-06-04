#!/usr/bin/python3
"""
Contain function "append_wrtie"
"""


def append_write(filename="", text=""):
    """return number of char append to "filename" from "text" """
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
