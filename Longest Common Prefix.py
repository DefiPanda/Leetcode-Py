class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        longest = strs[0]
        for str in strs[1:]:
            i = 0
            while i < len(str) and i < len(longest) and str[i] == longest[i]:
                i += 1
            longest = longest[:i]
        return longest