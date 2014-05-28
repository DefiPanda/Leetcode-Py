class Solution:
    def reverse(self, x):
        sign = 1
        result = 0
        if x < 0:
            sign = -1
            x = -x
        while x > 0:
            result = result * 10 + x % 10
            x /= 10
        return sign * result