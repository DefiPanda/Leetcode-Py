class Solution:
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        prev, prev_prev = 1, 0
        for i in range(len(s)):
            current = 0
            if s[i] != '0':
                current = prev
            if i > 0 and (s[i - 1] == "1" or (s[i - 1] == "2" and s[i] <= "6")):
                current += prev_prev
            prev, prev_prev = current, prev
        return prev