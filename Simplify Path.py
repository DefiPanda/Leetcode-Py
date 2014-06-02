class Solution:
    def simplifyPath(self, path):
        stack, tokens = [], path.split('/')
        for token in tokens:
            if token == "..":
                if len(stack) > 0:
                    stack.pop()
            elif token != "" and token != ".":
                stack.append(token)
        return "/" + reduce(lambda acc, x: acc + x + "/", stack, "")[:-1]