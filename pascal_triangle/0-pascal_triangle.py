#!/usr/bin/python3
"""Module for generating Pascal's Triangle."""

def pascal_triangle(n):
    """Generate Pascal's Triangle of size n.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list of lists of int: A list of lists representing Pascal's Triangle.
        Returns empty list if n <= 0.
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle