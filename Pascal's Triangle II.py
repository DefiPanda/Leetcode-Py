class Solution:
    def getRow(self, numRows):
        result = [1]
        for i in range(1, numRows + 1):
            current = [1]
            for j in range(1, i):
                current.append(result[j] + result[j - 1])
            result = current + [1]
        return result