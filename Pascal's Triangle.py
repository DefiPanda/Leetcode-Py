class Solution:
    def generate(self, numRows):
        result = [[1]]
        if numRows <= 0:
            return []
        for i in range(1, numRows):
            current = [1]
            for j in range(1, i):
                current.append(result[i - 1][j] + result[i - 1][j - 1])
            current.append(1)
            result.append(current)
        return result