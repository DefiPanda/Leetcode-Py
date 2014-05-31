class Solution:
    def longestValidParentheses(self, s):
        longest, last, indices = 0, 0, []
        for i in range(len(s)):
            if s[i] == '(':
                indices.append(i)
            elif len(indices) == 0:
                last = i + 1
            else:
                index = indices.pop()
                if len(indices) == 0:
                    longest = max(longest, i - last + 1)
                else:
                    longest = max(longest, i - indices[-1])
        return longest