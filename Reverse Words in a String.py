class Solution:
    def reverseWords(self, s):
        return " ".join(filter(None, reversed(s.split(" "))))
