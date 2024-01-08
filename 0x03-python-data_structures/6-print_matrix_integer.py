#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for val in matrix:
        print(' '.join('{}'.format(j)for j in val))
