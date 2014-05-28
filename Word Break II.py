class Solution:  
    def canBreak(self, s, dict):
        possible = []
        for i in range(len(s)):
            if s[:i + 1] in dict:
                possible.append(True)
            else:
                found = False
                for j in range(i):
                    if possible[j] == True and s[j + 1: i + 1] in dict:
                        found = True
                        break
                possible.append(found)
        return possible[len(s) - 1]
        
    def wordBreak(self, s, dict):
        result = {}
        if not self.canBreak(s, dict):
            return []
        for i in range(len(s)):
            result[s[:i + 1]] = []
            if s[:i + 1] in dict:
                result[s[:i + 1]] = [s[:i + 1]]
            for j in range(i):
                if s[:j + 1] in result and s[j + 1: i + 1] in dict:
                    for k in result[s[:j + 1]]:
                        result[s[:i + 1]].append(k + " " + s[j + 1: i + 1])
        return result[s]