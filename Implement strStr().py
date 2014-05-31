class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            found = True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    found = False
                    break
            if found:
                return haystack[i:]
        return None