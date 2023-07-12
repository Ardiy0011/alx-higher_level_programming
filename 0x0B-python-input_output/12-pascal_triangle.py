#!/usr/bin/python3
"""
function that prints pascals triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row[j] = prev_row[j - 1] + prev_row[j]
        triangle.append(row)

    for row in triangle:
        print(row)
