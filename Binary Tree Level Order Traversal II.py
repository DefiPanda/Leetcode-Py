class Solution:
    def levelOrderBottom(self, root):
        if root is None:
            return []
        res, current = [], [root]
        while current:
            next, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            current = next
            res.insert(0, vals)
        return res

    # def levelOrderBottom(self, root):
    #     """ Using a queue is also fine.
    #     """
    #     if root is None:
    #         return []
    #     current, res = [root], []
    #     while current:
    #         vals, length = [], len(current)
    #         for i in range(length):
    #             node = current[0]
    #             vals.append(node.val)
    #             if node.left:
    #                 current.append(node.left)
    #             if node.right:
    #                 current.append(node.right)
    #             current.pop(0)
    #         res.insert(0, vals)
    #     return res