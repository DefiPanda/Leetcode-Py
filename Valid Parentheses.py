class Solution:
    def isValid(self, parentheses):
        stack, lookup = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in parentheses:
            if parenthese in lookup:
                stack.append(parenthese)
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                return False
        return len(stack) == 0