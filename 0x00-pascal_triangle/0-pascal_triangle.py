#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """ Function that returns a list of lists of integers """

    if n <= 0:
        return []  # Return an empty list for non-positive n

    triangle = []
    for i in range(n):
        row = [1]  # First element is always 1
        for j in range(1, i):
            # Calculate the next element based on the previous row
            next_val = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(next_val)
        if i > 0:
            row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
