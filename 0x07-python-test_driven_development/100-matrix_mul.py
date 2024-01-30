#!/usr/bin/python3

"""

Defines a Module of matrix multiplication.

"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.

    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Both m_a and m_b must be lists")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("Both m_a and m_b must be lists of lists")

    if m_a == [] or m_a == [[]] or m_b == [] or m_b == [[]]:
        raise ValueError("Both matrices must be non-empty")

    if not all(isinstance(ele, (int, float)) for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(ele, (int, float)) for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("Each row of m_a and m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b cannot be multiplied")

    inverted_b = [[m_b[c][r] for c in range(len(m_b))] for r in range(len(m_b[0]))]

    new_matrix = [[sum(row[i] * col[i] for i in range(len(inverted_b[0]))) for col in inverted_b] for row in m_a]

    return new_matrix

