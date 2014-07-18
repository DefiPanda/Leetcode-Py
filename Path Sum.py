class Solution:
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        if root.left is None and root.right is None and sum == root.val:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)