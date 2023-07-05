#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    
    """Multiply two matrices.

    Args:
        m_a : The first matrix.
        m_b : The second matrix.
    Raises:
        TypeError: If  m_a or m_b isnt a list of lists of ints/floats.
        TypeError: If  m_a or m_b is empty.
        TypeError: If  m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """
    try:
        if m_a == [] or m_a == [[]]:
            raise ValueError("m_a can't be empty")
        if m_b == [] or m_b == [[]]:
            raise ValueError("m_b can't be empty")

        if not isinstance(m_a, list):
            raise TypeError("m_a must be a list")
        if not isinstance(m_b, list):
            raise TypeError("m_b must be a list")

        if not any(isinstance(row, list) for row in m_a):
            raise TypeError("m_a must be a list of lists")
        if not any(isinstance(row, list) for row in m_b):
            raise TypeError("m_b must be a list of lists")

        if not all(isinstance(num, (int, float)) for row in m_a for num in row):
            raise TypeError("m_a should contain only integers or floats")
        if not all(isinstance(num, (int, float)) for row in m_b for num in row):
            raise TypeError("m_b should contain only integers or floats")

        if not all(len(row) == len(m_a[0]) for row in m_a):
            raise TypeError("each row of m_a must should be of the same size")
        if not all(len(row) == len(m_b[0]) for row in m_b):
            raise TypeError("each row of m_b must should be of the same size")

        if len(m_a[0]) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")

        inverted_b = []
        for r in range(len(m_b[0])):
            new_row = []
            for c in range(len(m_b)):
                new_row.append(m_b[c][r])
            inverted_b.append(new_row)

        new_matrix = []
        for row in m_a:
            new_row = []
            for i in range(len(inverted_b[0])):
                prod = 0
                for j in range(len(inverted_b)):
                    prod += row[j] * inverted_b[i][j]
                new_row.append(prod)
            new_matrix.append(new_row)

        return new_matrix
    except (TypeError, ValueError) as r:
        print(r)

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
