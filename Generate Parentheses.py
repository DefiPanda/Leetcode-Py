class Solution:
    def generateParenthesis(self, n):
        result = []
        self.generateParenthesisRecur(result, "", n, n)
        return result
        
    def generateParenthesisRecur(self, result, current, left, right):
        if left == 0 and right == 0:
            result.append(current)
        if left > 0:
            self.generateParenthesisRecur(result, current + "(", left - 1, right)
        if left < right:
            self.generateParenthesisRecur(result, current + ")", left, right - 1)