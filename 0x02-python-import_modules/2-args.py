#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    n = len(argv)
    if n == 0:
        print("0 argument.")
    elif n == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(n))
    if n > 0:
        for i in range(1, n):
            print("{}: {}".format(i, argv[i]))
