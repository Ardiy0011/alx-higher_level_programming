#!/usr/bin/python3
import numpy as np
"""Defines a matrix multiplication function using NumPy."""

def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a : The first matrix.
        m_b : The second matrix.
    """

    return np.matmul(m_a, m_b)
