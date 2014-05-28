class Solution:
    def numTrees(self, n):
        count = [1, 1]
        for i in range(2, n + 1):
            tmp = 0
            for j in range(1, i + 1):
                tmp += count[j - 1] * count[i - j]
            count.append(tmp)
        return count[n]