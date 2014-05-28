class Solution:
    def sumNumbers(self, root):
        return self.sumNumbersRecur(root, 0)

    def sumNumbersRecur(self, root, sum):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 10 * sum + root.val
        return self.sumNumbersRecur(root.left, 10 * sum + root.val) + self.sumNumbersRecur(root.right, 10 * sum + root.val)