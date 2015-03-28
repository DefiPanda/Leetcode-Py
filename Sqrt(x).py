class Solution:
    def sqrt(self, x):
        if x <= 1:
            return x;
        y0 = x >> 1
        y = (y0 + x / y0) >> 1
        while y < y0:
            y0 = y
            y = (y0 + x / y0) >> 1
        return min(y, y0)
