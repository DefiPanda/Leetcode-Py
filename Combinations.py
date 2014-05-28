class Solution:
    def combine(self, n, k):
        return self.combineRecur([], n, k, 1)
        
    def combineRecur(self, current, n, k, i):
        if k == 0:
            return [current]
        if i > n:
            return []
        return self.combineRecur(current, n, k, i + 1) + self.combineRecur(current + [i], n, k - 1, i + 1)