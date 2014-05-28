class Solution:
    def reverseWords(self, s):
        return " ".join(filter(lambda x: x != "",reversed(s.split(" "))))