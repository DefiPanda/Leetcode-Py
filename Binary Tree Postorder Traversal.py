class Solution:
    def postorderTraversal(self, root):
        res, stack, current, prev = [], [], root, None
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                parent = stack[-1]
                if parent.right in (None, prev):
                    prev = stack.pop()
                    res.append(prev.val)
                else:
                    current = parent.right
        return res