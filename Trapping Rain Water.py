class Solution:
    def trap(self, A):
        left_max, left_maxes, right_max, right_maxes, water = 0, [], 0, [], 0
        for i in range(len(A)):
            left_maxes.append(left_max)
            left_max = max(A[i], left_max)
        for i in reversed(range(len(A))):
            right_maxes.insert(0, right_max)
            right_max = max(A[i], right_max)
        for i in range(len(A)):
            water += max(0, min(left_maxes[i], right_maxes[i]) - A[i])
        return water

    # def trap(self, A):
    #     """ My mania for functional programming needs a serious rest
    #     """
    #     left_highests, left_highest = [], 0
    #     for i in range(len(A)):
    #         left_highest = max(left_highest, A[i])
    #         left_highests.append(left_highest)
    #     right_highests, right_highest = [0 for i in range(len(A))], 0
    #     for i in reversed(range(len(A))):
    #         right_highest = max(right_highest, A[i])
    #         right_highests[i] = right_highest
    #     return reduce(lambda acc, i: acc + max(0, min(left_highests[i], right_highests[i]) - A[i]), range(len(A)), 0)