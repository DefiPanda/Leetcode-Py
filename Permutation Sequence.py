class Solution:
    def getPermutation(self, n, k):
        seq, k, fact = "", k - 1, math.factorial(n - 1)
        perm = [i for i in range(1, n + 1)]
        for i in reversed(range(n)):
            curr = perm[k / fact]
            seq += str(curr)
            perm.remove(curr)
            if i > 0:
                k %= fact
                fact /= i
        return seq