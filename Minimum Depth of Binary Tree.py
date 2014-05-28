class Solution:
    def minDepth(self, root):
        if root == None:
            return 0
        left_nodes = self.minDepth(root.left)
        right_nodes = self.minDepth(root.right)
        if left_nodes == 0 or right_nodes == 0:
            return 1 + left_nodes + right_nodes
        return 1 + min(left_nodes, right_nodes)