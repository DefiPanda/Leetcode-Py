class Solution:
    def atoi(self, str):
        i, sign, ret = 0, 1, 0
        if len(str) == 0:
            return 0
        while i < len(str) and str[i] == ' ':
            i += 1
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            sign = -1
            i += 1
        while i < len(str) and str[i] >= '0' and str[i] <= '9':
            ret = ret * 10 + ord(str[i]) - ord('0')
            i += 1
        return max(min(ret * sign, 2147483647), -2147483648)