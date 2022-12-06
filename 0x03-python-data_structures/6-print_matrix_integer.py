#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for line in matrix:
            print(" ".join("{:d}".format(j) for j in line))
    else:
        print("")
