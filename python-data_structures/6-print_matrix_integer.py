#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        return
    
    for i in range(len(matrix)):
        print("{}".format(matrix[i]))
        
