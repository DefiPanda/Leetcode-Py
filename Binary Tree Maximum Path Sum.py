class Solution:
    maxSum = -2147483648
    def maxPathSum(self, root):
        self.maxPathRecur(root)
        return self.maxSum
        
    def maxPathRecur(self, root):
        if root == None:
            return 0
        left = max(0, self.maxPathRecur(root.left))
        right = max(0, self.maxPathRecur(root.right))
        self.maxSum = max(self.maxSum, left + right + root.val)
        return root.val + max(left, right)