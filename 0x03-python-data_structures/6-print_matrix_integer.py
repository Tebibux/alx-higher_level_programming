#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    size = len(matrix)
    if size == 0:
        print('$')
    for i in range(size):
        iSize = len(matrix[i])
        for j in range(iSize):
            if j != 0:    
                print(" ", end='')
            print("{}".format(matrix[i][j]), end='')
            if j == (size - 1):
                print('', end='$')
        print()
