class Solution:
    def permuteUnique(self, num):
        solutions = [[]]
        for number in num:
            next = []
            for solution in solutions:
                for i in range(len(solution) + 1):
                    candidate = solution[:i] + [number] + solution[i:]
                    if candidate not in next:
                        next.append(candidate)
            solutions = next
        return solutions