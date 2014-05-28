class Solution:
    def isValidBST(self, root):
        return self.isValidBSTRecur(root, 2147483647, -2147483648)
        
    def isValidBSTRecur(self, root, max, min):
        if root == None:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.isValidBSTRecur(root.left, root.val, min) and self.isValidBSTRecur(root.right, max, root.val)