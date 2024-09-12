#!/usr/bin/python3
"""
Initiation of the code
"""


def rotate_2d_matrix(matrix):
    """ n rotation of 2d matrix"""

    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
