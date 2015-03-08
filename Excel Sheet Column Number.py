class Solution:
    def titleToNumber(self, s):
        num = 0
        for i in s:
            num *= 26
            num += ord(i) - 64
        return num
