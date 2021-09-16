#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    temp_matrix = []

    for row in matrix:
        temp_matrix.append([row[i]*row[i] for i in range(len(matrix))])

    return(temp_matrix)
