#!/usr/bin/python3

#Matrix Intege

def print_matrix_integer(matrix=[[]]):
    for num in range(len(matrix)):
        for num2 in range(len(matrix[num])):
            Mprint("{:d}".format(matrix[num][num2j]), end="")
            if num2 != (len(matrix[num]) - 1):
                print(" ", end="")

        print("")
