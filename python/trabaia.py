matr = list[list[float | int]]

# transformar em classe?

# 🤨
# :)
# (。﹏。*)


#assim
def somar(matrix1, matrix2):
    assert(len(matrix1) == len(matrix2))

    ret_matrix = [[0 for i in range(len(matrix1[0]))] for j in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2)):
            ret_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return ret_matrix

# ou

class matrix:
    def __init__(self, size: tuple[int, int], value: None|matr = None):
        self.size = size

        if value == None:
            self.value = [[0 for i in range(size[0])] for j in range(size[1])]
        self.value = value
    
    def __add__(self, other: matr):
        assert(len(self) == len(other))

        ret_matrix = [[0 for i in range(len(self[0]))] for j in range(len(self))]

        for i in range(len(self)):
            for j in range(len(matrix2)):
                ret_matrix[i][j] = self[i][j] + other[i][j]
        
        return ret_matrix
    
    def __sub__(self, other: matr):
        assert(len(self) == len(other))

        ret_matrix = [[0 for i in range(len(self[0]))] for j in range(len(self))]

        for i in range(len(self)):
            for j in range(len(matrix2)):
                ret_matrix[i][j] = self[i][j] - other[i][j]
        
        return ret_matrix

    def __mult__(self, other: matr):
        # tenebroso, medo
        ...

    def __repr__(self):
        representation = ""

        for i in range(len(self)):
            for j in range(len(self)):
                representation += self.value[i][j] + " "
            representation += "\n"
        
        return representation