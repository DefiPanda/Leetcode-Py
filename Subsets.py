class Solution:
    def subsets(self, S):
        return self.subsetsRecur([], sorted(S))
    
    def subsetsRecur(self, current, S):
        if S:
            return self.subsetsRecur(current, S[1:]) + self.subsetsRecur(current + [S[0]], S[1:])
        return [current]