class Solution:
    def lengthOfLastWord(self, s):
        if s.strip() == "":
            return 0
        return len(filter(lambda x: x != "", s.split(" "))[-1])