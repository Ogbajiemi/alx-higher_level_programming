#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        l = 1
        for q in r:
            if l == len(r):
                print("{:d}".format(q), end="")
            else:
                print("{:d}".format(q), end=" ")
            l = l + 1
        print()
