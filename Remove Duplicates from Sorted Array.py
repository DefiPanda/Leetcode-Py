class Solution:
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        i = 0
        for j in range(1, len(A)):
            if A[i] != A[j]:
                i += 1
                A[i] = A[j]
        return i + 1