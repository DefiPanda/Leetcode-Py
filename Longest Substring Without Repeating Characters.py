class Solution:
    def lengthOfLongestSubstring(self, s):
        longest, start, visited = 0, 0, [False for i in range(256)]
        for i, char in enumerate(s):
            if visited[ord(char)] == False:
                visited[ord(char)] = True
            else:
                while s[start] != char:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            longest = max(longest, i - start + 1)
        return longest