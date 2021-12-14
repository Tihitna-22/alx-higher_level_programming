#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides all elements in the matrix by div"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for sub_list in matrix:
        if type(sub_list) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(sub_list)
        elif size != len(sub_list):
            raise TypeError("Each row of the matrix must have the same size")
        for i in sub_list:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(i / div, 2) for i in sub_list] for sub_list in matrix]
    return new_matrix
