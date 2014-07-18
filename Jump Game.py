class Solution:
    def canJump(self, A):
        reachable = 0
        for i in range(len(A)):
            if i > reachable:
                return False
            reachable = max(reachable, i + A[i])
        return True