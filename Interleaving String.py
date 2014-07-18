class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        interleave_matrix = [[False for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
        interleave_matrix[0][0] = True
        for i in range(1, len(s1) + 1):
            interleave_matrix[i][0] = interleave_matrix[i - 1][0] and s1[i - 1] == s3[i - 1]
        for i in range(1, len(s2) + 1):
            interleave_matrix[0][i] = interleave_matrix[0][i - 1] and s2[i - 1] == s3[i - 1]
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                interleave_matrix[i][j] = (interleave_matrix[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (interleave_matrix[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return interleave_matrix[-1][-1]