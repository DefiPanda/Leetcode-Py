class Solution:
    def permuteUnique(self, nums):
        solutions = [[]]
        for num in nums:
            next = []
            for solution in solutions:
                for i in range(len(solution) + 1):
                    candidate = solution[:i] + [num] + solution[i:]
                    if candidate not in next:
                        next.append(candidate)
            solutions = next
        return solutions