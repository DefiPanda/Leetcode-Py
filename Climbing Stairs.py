class Solution:
    def climbStairs(self, n):
        prev, current = 1, 0
        for i in range(n + 1):
            prev, current = current, prev + current
        return current