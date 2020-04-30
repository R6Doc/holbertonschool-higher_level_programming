#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    l = len(sys.argv) - 1
    if l == 1:
        print("1 argument")
    elif l == 0:
        print("0 arguments")
    else:
        print("{} arguments:".format(l))
    a = 0
    for arg in sys.argv:
        if a != 0:
            print(a,": ", l)
        a += 1
