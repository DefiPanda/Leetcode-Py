class Solution:
    def twoSum(self, num, target):
        map = {}
        for i in range(len(num)):
            if target - num[i] in map:
                return (map[target - num[i]] + 1, i + 1)
            map[num[i]] = i
        return None