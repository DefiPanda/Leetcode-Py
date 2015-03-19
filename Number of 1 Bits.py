class Solution:
    def hammingWeight(self, n):
        weight = 0
        while n != 0:
            if n%2:
                weight += 1
            n = n >> 1
        return weight
