class Solution:
    def generateParenthesis(self, n):
        result = []
        self.generateRecur(result, n, 0, 0, "")
        return result
        
    def generateRecur(self, result, n, left, right, current):
        if left == n and right == n:
            result.append(current)
        if left < n:
            self.generateRecur(result, n, left + 1, right, current + "(")
        if right < left:
            self.generateRecur(result, n, left, right + 1, current + ")")