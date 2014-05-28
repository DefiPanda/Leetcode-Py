class Solution:
    def backtrack(self, result, trace, path, word):
        if len(trace[word]) == 0:
            result.append([word] + path)
        else:
            for prev in trace[word]:
                self.backtrack(result, trace, [word] + path, prev)
                    
    def findLadders(self, start, end, dict):
        result, trace, current, length = [], {word: [] for word in dict}, set([start]), len(start)
        while len(current) > 0:
            for i in current:
                dict.remove(i)
            next = set([])
            for word in current:
                for i in range(length):
                    before, after = word[:i], word[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i] != j:
                            candidate = before + j + after
                            if candidate in dict:
                                trace[candidate].append(word)
                                next.add(candidate)
            current = next
            if len(current) == 0:
                return []
            if end in current:
                break
        self.backtrack(result, trace, [], end)
        return result