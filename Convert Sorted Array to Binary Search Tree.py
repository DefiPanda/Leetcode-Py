class Solution:
    def sortedArrayToBST(self, num):
        return self.buildBST(num, 0, len(num) - 1)
    
    def buildBST(self, num, left, right):
        if left > right:
            return None
        mid = (left + right) / 2
        current = TreeNode(num[mid])
        current.left = self.buildBST(num, left, mid - 1)
        current.right = self.buildBST(num, mid + 1, right)
        return current