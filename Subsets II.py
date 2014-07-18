class Solution:
    def subsetsWithDup(self, S):
        results = []
        self.subsetsRecur(results, [], sorted(S))
        return results
    
    def subsetsRecur(self, results, result, S):
        if len(S) == 0 and result not in results:
            results.append(result)
        elif len(S):
            self.subsetsRecur(results, result, S[1:])
            self.subsetsRecur(results, result + [S[0]], S[1:])