#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    new_matrix = []
    for i in range(0, len(matrix)):
        list_1 = list(map(square, matrix[i]))
        new_matrix.append(list_1)

    return new_matrix


def square(x):
    return x**2
