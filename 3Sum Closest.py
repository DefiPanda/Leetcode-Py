class Solution:
    def threeSumClosest(self, A, target):
        A, result, closest_diff, i = sorted(A), 2147483647, 2147483647, 0
        while i < len(A) - 2:
            j, k = i + 1, len(A) - 1
            while j < k:
                diff = A[i] + A[j] + A[k] - target
                if diff < 0:
                    if math.fabs(diff) < math.fabs(closest_diff):
                        result, closest_diff = A[i] + A[j] + A[k], diff
                    j += 1
                elif diff > 0:
                    if math.fabs(diff) < math.fabs(closest_diff):
                        result, closest_diff = A[i] + A[j] + A[k], diff
                    k -= 1
                else:
                    return target
            i += 1
        return result