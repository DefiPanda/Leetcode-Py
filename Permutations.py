class Solution:
    def permute(self, num):
        solutions = [[]]
        for number in num:
            next = []
            for solution in solutions:
                for i in range(len(solution) + 1):
                    next.append(solution[:i] + [number] + solution[i:])
            solutions = next
        return solutions