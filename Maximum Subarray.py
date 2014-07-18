class Solution:
    def maxSubArray(self, A):
        global_max, local_max = -9223372036854775808, 0
        for x in A:
            local_max = local_max + x
            global_max = max(global_max, local_max)
            local_max = max(0, local_max)
        return global_max