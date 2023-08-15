#!/usr/bin/python3

# Matrix Intege

def print_matrix_integer(matrix=[[]]):
    for xx in range(len(matrix)):
        for yy in range(len(matrix[xx])):
            print("{:d}".format(matrix[xx][yy]), end="")
            if yy != (len(matrix[xx]) - 1):
                print(" ", end="")

        print("")
