#!/usr/bin/python3
"""this module defines a function that 
        appends to a file"""
def append_write(filename="", text=""):
    """this function appends to a file"""
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(text)
            return len(text)
    except FileNotFountError:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
            return len(text)
