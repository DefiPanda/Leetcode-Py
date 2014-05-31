class Solution:
    def lengthOfLongestSubstring(self, s):
        count, start, longest = [False for i in range(256)], 0, 0
        for i in range(len(s)):
            if count[ord(s[i])] == False:
                count[ord(s[i])] = True
            else:
                longest = max(i - start, longest)
                while s[start] != s[i]:
                    count[ord(s[start])] = False
                    start += 1
                start += 1
        longest = max(len(s) - start, longest)
        return longest