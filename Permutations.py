class Solution:
    def permute(self, nums):
        solutions = [[]]
        for num in nums:
            next = []
            for solution in solutions:
                for i in range(len(solution) + 1):
                    next.append(solution[:i] + [num] + solution[i:])
            solutions = next
        return solutions

    # Recursive Solution
    # def permute(self, nums):
    #     res = []
    #     self.permuteRecur(res, [], nums)
    #     return res
        
    # def permuteRecur(self, res, current, nums):
    #     if len(nums) == 0:
    #         res.append(current)
    #         return
    #     for i in range(len(current) + 1):
    #         self.permuteRecur(res, current[:i] + [nums[0]] + current[i:], nums[1:])