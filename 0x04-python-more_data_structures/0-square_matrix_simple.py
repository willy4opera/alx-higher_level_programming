#!/usr/bin/python3

# computes the square value of all integers of a matrix

def square_matrix_simple(matrix=[]):
    return ([list(map(lambda a: a * a, row)) for row in matrix])
