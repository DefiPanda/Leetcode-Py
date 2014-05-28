class Solution:
    # Constant space solution
    def setZeroes(self, matrix):
        first_row = reduce(lambda acc, i: acc or matrix[0][i] == 0, range(len(matrix[0])), False)
        first_col = reduce(lambda acc, i: acc or matrix[i][0] == 0, range(len(matrix)), False)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                     matrix[i][j] = 0
        if first_col == True:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if first_row == True:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0