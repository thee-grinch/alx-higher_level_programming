#!/usr/bin/python3
"""this module defines a function"""


def pascal_triangle(n):
    """this function computes a pascal triangle"""
    if n  <= 0:
        return []
    triangle_list = [[1]]
    for a in range(n):
        buffer = triangle_list[a]
        tmp = [1]
        for i in range(len(buffer) - 1):
            tmp.append(buffer[i] + buffer[i + 1])
        tmp.append(1)
        triangle_list.append(tmp)
    return triangle_list
