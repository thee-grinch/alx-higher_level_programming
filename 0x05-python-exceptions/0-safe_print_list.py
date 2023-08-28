#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """attempts to safely print a list"""
    try:
        count = 0
        for item in range(x):
            print(f"{my_list[item]}", end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()
    return count
