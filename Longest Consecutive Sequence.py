class Solution:
    def longestConsecutive(self, num):
        visited, sequence, count = set([]), set(num), {}
        for x in num:
            if x in visited:
                continue
            count[x] = 1
            left, right = x - 1, x + 1
            while right in sequence:
                visited.add(right)
                count[x] += 1
                right += 1
            while left in sequence:
                visited.add(left)
                count[x] += 1
                left -=1
            visited.add(x)
        return reduce(max, count.values())