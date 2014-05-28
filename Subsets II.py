class Solution:
    def subsetsWithDup(self, S):
        result = []
        self.subsetsRecur(result, [], sorted(S), 0)
        return result
        
    def subsetsRecur(self, result, current, S, i):
        if i == len(S) and current not in result:
            result.append(current)
        elif i < len(S):
            self.subsetsRecur(result, current, S, i + 1)
            self.subsetsRecur(result, current + [S[i]], S, i + 1)