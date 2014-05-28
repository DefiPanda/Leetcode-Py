class Solution:
    def minDistance(self, word1, word2):
        lookup = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            lookup[i][0] = i
        for j in range(1, len(word2) + 1):
            lookup[0][j] = j
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                lookup[i][j] = min(lookup[i - 1][j] + 1, lookup[i][j - 1] + 1, lookup[i - 1][j - 1] + (word1[i - 1] != word2[j - 1]))
        return lookup[len(word1)][len(word2)]