class Solution:
    def searchRange(self, A, target):
        start, end, range = 0, len(A) - 1, []
        while start < end:
            mid = (start + end) / 2
            if target <= A[mid]:
                end = mid
            else:
                start = mid + 1
        if A[start] != target:
            return [-1, -1]
        range.append(start)
        start, end = 0, len(A)
        while start < end:
            mid = (start + end) / 2
            if target >= A[mid]:
                start = mid + 1
            else:
                end = mid
        return range + [start - 1]