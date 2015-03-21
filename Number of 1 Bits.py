class Solution:
    def hammingWeight(self, n):
        count = 0
        while n:
            count += 1
            n = (n - 1) & n
        return count
