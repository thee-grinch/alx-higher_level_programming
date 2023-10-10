#!/usr/bin/python3
"""this module defines a function"""


def read_file(filename=""):
    """this function reads a text file and prints it to """

    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            print({}.format(line))
