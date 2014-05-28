class Solution:
    def jump(self, A):
        step, reachable, i = -1, 0, 0
        while i < len(A) and i <= reachable:
            next_reachable = 0
            while i <= reachable and i < len(A):
                next_reachable = max(next_reachable, A[i] + i)
                i += 1
            reachable = next_reachable
            step += 1
        return step