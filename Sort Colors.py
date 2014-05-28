class Solution:
    def sortColors(self, A):
        i, zero_boundary, two_boundary = 0, -1, len(A)
        while i < two_boundary:
            if A[i] == 0:
                zero_boundary += 1
                A[zero_boundary], A[i] = A[i], A[zero_boundary]
            elif A[i] == 2:
                two_boundary -= 1
                A[two_boundary], A[i] = A[i], A[two_boundary]
                i -= 1
            i += 1