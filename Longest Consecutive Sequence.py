class Solution:
    def longestConsecutive(self, nums):
        lookup, longest = {num: False for num in nums}, 0
        for num in lookup:
            if lookup[num] == False:
                lookup[num] = True
                consecutive, i, j = 1, num + 1, num - 1
                while i in lookup and lookup[i] == False:
                    consecutive += 1
                    lookup[i] = True
                    i += 1
                while j in lookup and lookup[j] == False:
                    consecutive += 1
                    lookup[j] = True
                    j -= 1
                longest = max(longest, consecutive)
        return longest

    # def longestConsecutive(self, num):
    #     """Using visited set is also fine.
    #     """
    #     visited, sequence, count = set([]), set(num), {}
    #     for x in num:
    #         if x in visited:
    #             continue
    #         count[x] = 1
    #         left, right = x - 1, x + 1
    #         while right in sequence:
    #             visited.add(right)
    #             count[x] += 1
    #             right += 1
    #         while left in sequence:
    #             visited.add(left)
    #             count[x] += 1
    #             left -=1
    #         visited.add(x)
    #     return reduce(max, count.values())