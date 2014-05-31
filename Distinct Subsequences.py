class Solution:
    def numDistinct(self, S, T):
        ways = [[0 for j in range(len(S) + 1)] for i in range(len(T) + 1)]
        for i in range(len(S) + 1):
            ways[0][i] = 1
        for i in range(1, len(T) + 1):
            for j in range(1, len(S) + 1):
                ways[i][j] = ways[i][j - 1]
                if T[i - 1] == S[j - 1]:
                    ways[i][j] += ways[i - 1][j - 1]
        return ways[len(T)][len(S)]