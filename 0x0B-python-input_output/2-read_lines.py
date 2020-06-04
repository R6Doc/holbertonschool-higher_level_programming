#!/usr/bin/python3
"""
Contain read_lines function
"""


def read_lines(filename="", nb_lines=0):
    """read lines of a text file and prints to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
            return
        i = 0
        for i, line in enumerate(f):
            if i == nb_lines:
                break
            print(line, end='')
