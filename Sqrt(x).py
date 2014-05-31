class Solution:
    def sqrt(self, x):
        low, high = 0, x / 2 + 1
        while high >= low:
            mid = (high + low) / 2
            if x < mid * mid:
                high = mid - 1
            else:
                low = mid + 1
        return int(high)