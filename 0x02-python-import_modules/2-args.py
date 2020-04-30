#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    l = len(sys.argv)
    print("{:d} {:s}{:s}".format(l - 1, "argument" if l <= 2 else "arguments",
                                 "." if l == 1 else ":"))
    for i, s in enumerate(sys.argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
