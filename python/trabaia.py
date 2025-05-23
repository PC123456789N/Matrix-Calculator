from __future__ import annotations

import random

class matrix:
    def __init__(self: matrix, size: tuple[int, int], value: None|matrix = None):
        self.size = size

        if value == None:
            self.value = [[0 for i in range(size[1])] for j in range(size[0])]
        else:
            self.value = value
    
    def __add__(self: matrix, other: matrix):
        assert(len(self) == len(other))

        ret_matrix = [[0 for i in range(len(self[0]))] for j in range(len(self))]

        for i in range(len(self)):
            for j in range(len(other)):
                ret_matrix[i][j] = self[i][j] + other[i][j]
        
        return ret_matrix
    
    def __sub__(self: matrix, other: matrix):
        assert(len(self) == len(other))

        ret_matrix = [[0 for i in range(len(self[0]))] for j in range(len(self))]

        for i in range(len(self)):
            for j in range(len(other)):
                ret_matrix[i][j] = self[i][j] - other[i][j]
        
        return ret_matrix

    def __mul__(self, other: matrix) -> matrix:
        assert(self.size[0] == other.size[1])

        new_matrix: matrix = matrix((self.size[0], other.size[1]))

        for i in range(self.size[0]):
            for j in range(other.size[1]):
                for k in range(self.size[1]):
                    new_matrix.value[i][j] += self.value[i][k] * other.value[k][j]
        
        return new_matrix

    def __repr__(self: matrix):
        representation = ""

        for i in range(len(self.value)):
            for j in range(len(self.value[0])):
                representation += str(self.value[i][j]) + " "
            representation += "\n"
        
        return representation

def rand_matrix(size, start, stop) -> matrix:
    mat = matrix(size)

    for i in range(mat.size[0]):
        for j in range(mat.size[1]):
            mat.value[i][j] = random.randint(start, stop)
    
    return mat