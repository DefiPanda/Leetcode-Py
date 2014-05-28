class Solution:
    def trap(self, A):
        left_highests, left_highest = [], 0
        for i in range(len(A)):
            left_highest = max(left_highest, A[i])
            left_highests.append(left_highest)
        right_highests, right_highest = [0 for i in range(len(A))], 0
        for i in reversed(range(len(A))):
            right_highest = max(right_highest, A[i])
            right_highests[i] = right_highest
        return reduce(lambda acc, i: acc + max(0, min(left_highests[i], right_highests[i]) - A[i]), range(len(A)), 0)