class Solution:
    def minimumTotal(self, triangle):
        if len(triangle) == 0:
            return 0
        current = triangle[0]
        for i in range(1, len(triangle)):
            next = []
            next.append(triangle[i][0] + current[0])
            for j in range(1, i):
                next.append(triangle[i][j] + min(current[j - 1], current[j]))
            next.append(triangle[i][-1] + current[-1])
            current = next
        return reduce(min, current)