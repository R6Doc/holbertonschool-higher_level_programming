#!/usr/bin/python3
"""
Contain read_file function
"""


def read_file(filename=""):
    """""read text file and prints to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
