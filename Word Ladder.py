class Solution:
    def ladderLength(self, start, end, dict):
        current, distance, visited, faster_dict = [start], 1, {start:0}, {}
        dict.add(end)
        for word in dict:
            faster_dict[word] = 0
        while len(current) > 0:
            next = []
            for word in current:
                for i in xrange(len(word)):
                    before, after = word[:i], word[i + 1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = before + j + after
                        if candidate in faster_dict and candidate not in visited:
                            if candidate == end:
                                return distance + 1
                            visited[candidate] = 0
                            next.append(candidate)
            current, distance = next, distance + 1
        return 0