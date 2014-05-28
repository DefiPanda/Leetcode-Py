class Solution:
    def isValid(self, s):
        lookup, stack = {")": "(", "}": "{", "]": "["}, []
        for i in s:
            if i not in lookup:
                stack.append(i)
            else:
                if len(stack) == 0 or stack.pop() != lookup[i]:
                    return False
        return len(stack) == 0