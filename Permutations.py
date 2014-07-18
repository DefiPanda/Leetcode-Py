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