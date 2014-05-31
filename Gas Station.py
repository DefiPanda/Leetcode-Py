class Solution:
    def canCompleteCircuit(self, gas, cost):
        start, sum_so_far, sum = 0, 0, 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            if sum_so_far + diff < 0:
                start = i + 1
                sum_so_far = 0
            else:
                sum_so_far += diff
            sum += diff
        if sum >= 0:
            return start
        return -1