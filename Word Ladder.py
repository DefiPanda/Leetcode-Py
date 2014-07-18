class Solution:
    def ladderLength(self, start, end, dict):
        distance, current, visited = 0, [start], set([start])
        dict.add(end)
        while current:
            next = []
            for word in current:
                if word == end:
                    return distance + 1
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate not in visited and candidate in dict:
                            next.append(candidate)
                            visited.add(candidate)
            distance += 1
            current = next
        return 0