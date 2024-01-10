#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_sq = []
    for val in matrix:
        matrix_sq.append([i**2 for i in val])
    return matrix_sq
