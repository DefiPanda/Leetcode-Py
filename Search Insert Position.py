class Solution:
    def bianrySearch(self, A, target, low, hi):
        mid = (low + hi) / 2
        if low > hi:
            return low
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            return self.bianrySearch(A, target, mid + 1, hi)
        else:
            return self.bianrySearch(A, target, low, mid - 1)
        return mid
        
    def searchInsert(self, A, target):
        return self.bianrySearch(A, target, 0, len(A) - 1)