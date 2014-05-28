class Solution:
    def pathSum(self, root, sum):
        return self.pathSumRecur([], [], root, sum)
        
    def pathSumRecur(self, result, current, root, sum):
        if root == None:
            return result
        if root.val == sum and root.left == None and root.right == None:
            return result + [current + [root.val]]
        return self.pathSumRecur(result, current + [root.val], root.left, sum - root.val) + self.pathSumRecur(result, current + [root.val], root.right, sum - root.val)