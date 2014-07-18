class Solution:
    def inorderTraversal(self, root):
        res, stack, current = [], [], root
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                parent = stack.pop()
                res.append(parent.val)
                current = parent.right
        return res