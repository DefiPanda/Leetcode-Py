class Solution:
    def searchInsert(self, A, target):
        return self.searchInsertRecur(A, target, 0, len(A) - 1)
        
    def searchInsertRecur(self, A, target, low, high):
        mid = (high + low) / 2
        if low > high:
            return low
        if A[mid] == target:
            return mid
        if A[mid] < target:
            return self.searchInsertRecur(A, target, mid + 1, high)
        else:
            return self.searchInsertRecur(A, target, low, mid - 1)

    # def searchInsert(self, A, target):
    #   """Iterative solution is also fine.
    #   """
    #     low, high = 0, len(A) - 1
    #     while low <= high:
    #         mid = (low + high) / 2
    #         if A[mid] == target:
    #             return mid
    #         elif A[mid] < target:
    #             low = mid + 1
    #         else:
    #             high = mid - 1
    #     return low