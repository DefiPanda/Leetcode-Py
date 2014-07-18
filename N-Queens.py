class Solution:
    def solveNQueens(self, n):
        solutions = []
        self.solveRecur(solutions, [], n, 0)
        return solutions
    
    def solveRecur(self, solutions, solution, n, row):
        if row == n:
            solutions.append(map(lambda x: '.' * x + "Q" + '.' * (n - x - 1), solution))
        for i in range(n):
            if i not in solution and reduce(lambda acc, j: abs(row - j) != abs(i - solution[j]) and acc, range(len(solution)), True):
                self.solveRecur(solutions, solution + [i], n, row + 1)
    
    # The alternative is to make one line reduce function a separate method. Either way is fine.
        
    # def is_diagonally_legal(self, solution, n, row, col):
    #     for i in range(len(solution)):
    #         if abs(row - i) == abs(col - solution[i]):
    #             return False
    #     return True
        
    # def solveNQueensRecur(self, solutions, solution, n, i):
    #     if i == n:
    #         solutions.append(map(lambda x: '.' * x + "Q" + '.' * (n - x - 1), solution))
    #     for j in range(n):
    #         if j not in solution and self.is_diagonally_legal(solution, n, i, j):
    #             self.solveNQueensRecur(solutions, solution + [j], n, i + 1)