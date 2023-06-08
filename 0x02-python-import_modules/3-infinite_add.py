#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    a = len(sys.argv) - 1
    b = 0

    for x in range(a):
        b += int(sys.argv[x + 1])
    print("{}".format(b))
