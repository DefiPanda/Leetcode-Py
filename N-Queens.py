class Solution:
    def solveNQueens(self, n):
        solutions = []
        self.solveRecur(solutions, [], n, 0)
        return solutions
    
    def solveRecur(self, solutions, solution, n, row):
        if row == n:
            solutions.append(map(lambda x: '.' * x + "Q" + '.' * (n - x - 1), solution))
        for i in range(n):
            if i not in solution and reduce(lambda acc, j: math.fabs(row - j) != math.fabs(i - solution[j]) and acc, range(len(solution)), True):
                self.solveRecur(solutions, solution + [i], n, row + 1)