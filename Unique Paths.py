class Solution:
    def uniquePaths(self, m, n):
        ways = [[1] for i in range(m)]
        for i in range(1, n):
            ways[0].append(1)
        for i in range(1, m):
            for j in range(1, n):
                ways[i].append(ways[i - 1][j] + ways[i][j - 1])
        return ways[m - 1][n - 1]