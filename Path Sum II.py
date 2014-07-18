class Solution:
    def pathSum(self, root, sum):
        return self.pathSumRecur([], [], root, sum)
        
    def pathSumRecur(self, result, path, root, sum):
        if root is None:
            return result
        if root.left is None and root.right is None and root.val == sum:
            return result + [path + [root.val]]
        return self.pathSumRecur(result, path + [root.val], root.left, sum - root.val) + self.pathSumRecur(result, path + [root.val], root.right, sum - root.val)