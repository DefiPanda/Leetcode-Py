class Solution:
    def totalNQueens(self, n):
        return self.solveRecur(0, [], n, 0)
    
    def solveRecur(self, solutions, solution, n, row):
        if row == n:
            return 1
        res = solutions
        for i in range(n):
            if i not in solution and reduce(lambda acc, j: math.fabs(row - j) != math.fabs(i - solution[j]) and acc, range(len(solution)), True):
                res += self.solveRecur(solutions, solution + [i], n, row + 1)
        return res