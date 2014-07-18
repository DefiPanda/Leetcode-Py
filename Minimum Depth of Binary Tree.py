class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left and root.right is None:
            return self.minDepth(root.left) + 1
        elif root.right and root.left is None:
            return self.minDepth(root.right) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    # def minDepth(self, root):
    # """ This method has better readability, but more recursive calls.
    # """
    #     if root == None:
    #         return 0
    #     left_nodes = self.minDepth(root.left)
    #     right_nodes = self.minDepth(root.right)
    #     if left_nodes == 0 or right_nodes == 0:
    #         return 1 + left_nodes + right_nodes
    #     return 1 + min(left_nodes, right_nodes)