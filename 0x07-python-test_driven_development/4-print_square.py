#!/usr/bin/python3
""" this module attempts to print a square using the hash (#)symbol"""
def print_square(size):
    """the function to print an integer of size size"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size <= 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        [print('#', end="") for _ in range(0, size)]
        if i != size - 1:
            print("")
