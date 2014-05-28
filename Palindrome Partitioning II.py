class Solution:
    def minCut(self, s):
        lookup, mincut = [[False for j in range(len(s))] for i in range(len(s))], [0 for i in range(len(s))]
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if s[i] == s[j]  and (j - i < 2 or lookup[i + 1][j - 1]):
                    lookup[i][j] = True
                else:
                    lookup[i][j] = False
        for i in range(len(s)):
            min_so_far = 2147483647
            if lookup[0][i] == False:
                for j in range(i):
                    if lookup[j + 1][i] == True:
                        min_so_far = min(min_so_far, mincut[j] + 1)
            else:
                min_so_far = 0
            mincut[i] = min_so_far
        return mincut[-1]