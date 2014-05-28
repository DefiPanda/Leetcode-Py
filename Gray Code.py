class Solution:
    def grayCode(self, n):
        return map(lambda x: (x / 2) ^ x, range(1 << n))