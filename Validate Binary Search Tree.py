class Solution:
    def isValidBST(self, root):
        return self.isValidBSTRecur(root, 9223372036854775807, -9223372036854775808)
        
    def isValidBSTRecur(self, root, upper, lower):
        if root is None:
            return True
        if root.val <= lower or root.val >= upper:
            return False
        return self.isValidBSTRecur(root.left, root.val, lower) and self.isValidBSTRecur(root.right, upper, root.val)