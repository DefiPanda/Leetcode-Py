class Solution:
    def subsets(self, S):
        return self.subsetsRecur([], sorted(S), 0)
        
    def subsetsRecur(self, current, S, i):
        if i == len(S):
            return [current]
        return self.subsetsRecur(current, S, i + 1) + self.subsetsRecur(current + [S[i]], S, i + 1)