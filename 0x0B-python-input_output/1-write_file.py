#!/usr/bin/python3
"""this module defines a function that writes to a file"""


def write_file(filename="", text=""):
    """function to write to a function"""
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
    written = len(text)
    return written
