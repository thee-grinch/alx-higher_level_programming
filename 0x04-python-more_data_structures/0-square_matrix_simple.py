#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """THIS FUNCTION SQUARES A MATRIX"""
    square = []
    for arr in matrix:
        square_array = list(map(lambda x: x * x, arr))
        square.append(square_array)
    return square
