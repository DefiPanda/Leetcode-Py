class Solution:
    def sortColors(self, A):
        i, last_zero, first_two = 0, -1, len(A) 
        while i < first_two:
            if A[i] == 0:
                last_zero += 1
                A[last_zero], A[i] = A[i], A[last_zero]
            if A[i] == 2:
                first_two -= 1
                A[first_two], A[i] = A[i], A[first_two]
                i -= 1
            i += 1