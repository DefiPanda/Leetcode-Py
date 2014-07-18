class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        current, res = [root], []
        while current:
            next, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            res.append(vals)
            current = next
        return res

    # def levelOrder(self, root):
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
    #         res.append(vals)
    #     return res