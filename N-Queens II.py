class Solution:
    def totalNQueens(self, n):
        return self.solveRecur([], n, 0)
        
    def solveRecur(self, solution, n, row):
        if row == n:
            return 1
        res = 0
        for i in range(n):
            if i not in solution and reduce(lambda acc, j: abs(row - j) != abs(i - solution[j]) and acc, range(len(solution)), True):
                res += self.solveRecur(solution + [i], n, row + 1)
        return res
        
    # The alternative is to make one line reduce function a separate method. Either way is fine.
        
    # def is_diagonally_legal(self, solution, n, row, col):
    #     for i in range(len(solution)):
    #         if abs(row - i) == abs(col - solution[i]):
    #             return False
    #     return True
        
    # def solveRecur(self, solution, n, col):
    #     if col == n:
    #         return 1
    #     total = 0
    #     for j in range(n):
    #         if j not in solution and self.is_diagonally_legal(solution, n, col, j):
    #             total += self.solveRecur(solution + [j], n, col + 1)
    #     return total