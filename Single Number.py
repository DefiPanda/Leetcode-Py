class Solution:
    def singleNumber(self, A):
        return reduce(operator.xor, A)