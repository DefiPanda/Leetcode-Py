class Solution:
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        if root.val == sum and root.left == None and root.right == None:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)