class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isSymmetricRecur(root.left, root.right)
        
    def isSymmetricRecur(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isSymmetricRecur(left.left, right.right) and self.isSymmetricRecur(left.right, right.left)