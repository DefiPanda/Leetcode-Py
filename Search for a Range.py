class Solution:
    def searchRange(self, A, target):
        left = self.searchRangeRecur(A, target, lambda x, y: x >= y, 0, len(A) - 1)
        if left >= len(A) or A[left] != target:
            return [-1, -1]
        right = self.searchRangeRecur(A, target, lambda x, y: x > y, 0, len(A) - 1) - 1
        return [left, right]
        
    def searchRangeRecur(self, A, target, compare, left, right):
        if left > right:
            return left
        mid = (left + right) / 2
        if compare(A[mid], target):
            return self.searchRangeRecur(A, target, compare, left, mid - 1)
        return self.searchRangeRecur(A, target, compare, mid + 1, right)

    def searchRange(self, A, target):
        """ The iterative solution is also fine.
        """
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