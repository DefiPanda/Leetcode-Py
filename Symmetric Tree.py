class Solution:
    def isSymmetric(self, root):
        if root == None:
            return True
        return self.isSymmetricRecur(root.left, root.right)
        
    def isSymmetricRecur(self, left, right):
        if left == None and right == None:
            return True
        if left == None or right == None or left.val != right.val:
            return False
        return self.isSymmetricRecur(left.left, right.right) and self.isSymmetricRecur(left.right, right.left)