class Solution:
    def maxSubArray(self, A):
        global_max, local_max = -9223372036854775808, 0
        for element in A:
            global_max = max(global_max, local_max + element)
            local_max = max(0, local_max + element)
        return global_max