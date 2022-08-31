#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    parent = []
    chiled = []
    for list in matrix:
        for item in list:
            chiled.append(item**2)
        parent.append(chiled)
        chiled = []
    return parent
