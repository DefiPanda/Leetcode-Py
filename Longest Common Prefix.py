class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        result, i = strs[0], 0
        while i < len(strs[0]):
            for str in strs:
                if i >= len(str) or str[i] != strs[0][i]:
                    return result[:i]
            i += 1
        return result