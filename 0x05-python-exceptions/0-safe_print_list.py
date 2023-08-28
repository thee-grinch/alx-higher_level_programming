#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """attempts to safely print a list"""
    try:
        i = 0
        for item in range(x):
            print(f"{my_list[item]}", end="")
            i += 1
        print()
        return i
    except IndexError:
        return i
