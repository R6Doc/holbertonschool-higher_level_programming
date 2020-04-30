#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    addition = 0
    for s in argv[1:]:
        addition += int(s)
    print("{:d}".format(addition))
