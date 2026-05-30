#!/usr/bin/python3
"""Module that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.

    Args:
        matrix (list): List of lists of integers/floats.
        div (int or float): Divisor.

    Returns:
        A new matrix with elements divided by div and rounded to 2 decimals.
    """
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_size = len(matrix[0])

    for row in matrix:
        if len(row) != row_size:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )

        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]