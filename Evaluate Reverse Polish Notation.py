class Solution:
    def evalRPN(self, tokens):
        numerals, operators = [], {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}
        for token in tokens:
            if token.isdigit() or token[1:].isdigit():
                numerals.append(int(token))
            else:
                x, y = numerals.pop(), numerals.pop()
                numerals.append(int(operators[token](y * 1.0, x)))
        return numerals.pop()