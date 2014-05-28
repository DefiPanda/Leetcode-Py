class Solution:
    def maxSubArray(self, A):
        overall_max, running_max = -9223372036854775808, 0
        for x in A:
            running_max += x
            if running_max > overall_max:
                overall_max  = running_max
            if running_max < 0:
                running_max = 0
        return overall_max