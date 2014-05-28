class Solution:
    def nextPermutation(self, num):
        k, l = -1, 0
        for i in range(len(num) - 1):
            if num[i] < num[i + 1]:
                k = i
        if k == -1:
            return num[::-1]
        for i in range(len(num)):
            if num[i] > num[k]:
                l = i
        num[k], num[l] = num[l], num[k]
        return num[:k + 1] + num[:k:-1]