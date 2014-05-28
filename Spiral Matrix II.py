class Solution:
    def generateMatrix(self, n):
        matrix = [[0 for i in range(n)] for i in range(n)]
        left, right, top, bottom, num = 0, n - 1, 0, n - 1, 1
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            for i in range(top + 1, bottom):
                matrix[i][right] = num
                num += 1
            for i in reversed(range(left, right + 1)):
                if top < bottom:
                    matrix[bottom][i] = num
                    num += 1
            for i in reversed(range(top + 1, bottom)):
                matrix[i][left] = num
                num += 1
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return matrix