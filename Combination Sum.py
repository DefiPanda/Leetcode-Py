class Solution:
    def combinationSum(self, candidates, target):
        result = []
        self.combinationSumRecur(sorted(candidates), result, [], 0, target)
        return result
        
    def combinationSumRecur(self, candidates, result, current, start, target):
        if target == 0:
            result.append(current)
        else:
            while start < len(candidates) and candidates[start] <= target:
                self.combinationSumRecur(candidates, result, current + [candidates[start]], start, target - candidates[start])
                start += 1