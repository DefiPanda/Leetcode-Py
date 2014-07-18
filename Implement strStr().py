class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return haystack[i:]
        return None