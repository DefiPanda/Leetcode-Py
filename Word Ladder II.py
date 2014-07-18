class Solution:
    def backtrack(self, result, trace, path, word):
        if len(trace[word]) == 0:
            result.append([word] + path)
        else:
            for prev in trace[word]:
                self.backtrack(result, trace, [word] + path, prev)
                
    def findLadders(self, start, end, dict):
        result, trace, current = [], {word: [] for word in dict}, set([start])
        while current and end not in current:
            for word in current:
                dict.remove(word)
            next = set([])
            for word in current:
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate in dict:
                            trace[candidate].append(word)
                            next.add(candidate)
            current = next
        if current:
            self.backtrack(result, trace, [], end)
        return result