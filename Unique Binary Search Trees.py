class Solution:
    def numTrees(self, n):
        counts = [1, 1]
        for i in range(2, n + 1):
            count = 0
            for j in range(0, i):
                count += counts[j] * counts[i - j - 1]
            counts.append(count)
        return counts[-1]