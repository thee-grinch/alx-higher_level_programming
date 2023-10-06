#!/usr/bin/python3
"""This module divides a matrix by a divisor and returns the matrix"""


def matrix_divided(matrix, div):
    """This function divides a matrix"""
    if matrix == []:
        return []
    if not (isinstance(matrix, list)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(x, list) for x in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    def err():
        """Raises a type error exception """
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    [[err() for x in row if not isinstance(x, (int, float))] for row in matrix]

    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in row] for row in matrix]
