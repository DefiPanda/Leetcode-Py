class Solution:
    def singleNumber(self, A):
        one, two, three = 0, 0, 0
        for i in range(len(A)):
            two |= one & A[i];
            one ^= A[i];
            three = one & two;
            one &= ~three;
            two &= ~three;
        return one;