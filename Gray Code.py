class Solution:
    def grayCode(self, n):
        return [(x / 2) ^ x for x in range(1 << n)]