#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for c in my_string:
        if c != 'C' and c != 'c':
            string += c
    return string
