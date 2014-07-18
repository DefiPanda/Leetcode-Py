class Solution:
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])