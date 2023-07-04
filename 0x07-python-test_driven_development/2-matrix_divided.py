#!/usr/bin/python3

"""
module that divides two integers at correspondning indexes within a matrix.
"""
def matrix_divided(matrix, div):
    """
    Function to divide two integers at correspondning indexes within a matrix.

    Args:
        a (matrix): the entire matrix/list of lists
        b (div): The divisor.

    Returns:
        list of ints/floats

    Raises:
        TypeError: If the elements in a mtrix aren't integers or floats
        TypeError: If each row of the matrix aren't the same size or length
        TypeError: If matrix is empty
        TypeError: If divisor is anything less than an integer or float
        ZeroDivisionError : if divisor is 0
           
    """
    try:
        if not all(isinstance(value, (int, float)) for row in matrix for value in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if any(len(row) != len(matrix[0]) for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")
        
        if len(matrix) == 0 :
           raise IndexError("empty matrix")

        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")

        if div == 0:
            raise ZeroDivisionError("division by zero")
        
        res = []
        bes = []
        for value in range(len(matrix[0])):
            result1 = matrix[0][value] / div
            result2 = matrix[1][value] / div
            res.append(round(result1, 2))
            bes.append(round(result2, 2))
        return list((res, bes))
    except (TypeError, ZeroDivisionError, IndexError) as e:
        return str(e)
