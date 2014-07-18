class Solution:
    def sortedArrayToBST(self, num):
        if len(num) == 0:
            return None
        mid = len(num) / 2
        current = TreeNode(num[mid])
        current.left = self.sortedArrayToBST(num[:mid])
        current.right = self.sortedArrayToBST(num[mid + 1:])
        return current