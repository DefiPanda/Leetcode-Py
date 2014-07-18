class Solution:
    def preorderTraversal(self, root):
        res, stack = [], [root]
        if root is None:
            return res
        while stack:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            res.append(current.val)
        return res