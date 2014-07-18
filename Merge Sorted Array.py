class Solution:
    def merge(self, A, m, B, n):
        last, i, j = m + n - 1, m - 1, n - 1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[last] = A[i]
                i, last = i - 1, last - 1
            else:
                A[last] = B[j]
                j, last = j - 1, last - 1
        while j >= 0:
            A[last] = B[j]
            j, last = j - 1, last - 1