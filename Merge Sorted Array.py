class Solution:
    def merge(self, A, m, B, n):
        last = m + n - 1
        while m > 0 and n > 0:
            if A[m - 1] >= B[n - 1]:
                A[last] = A[m - 1]
                m -= 1
            else:
                A[last] = B[n - 1]
                n -= 1
            last -= 1
        while n > 0:
            A[n - 1] = B[n - 1]
            n -= 1