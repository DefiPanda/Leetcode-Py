class Solution:
    def buildTree(self, inorder, postorder):
        # using dictionary for index lookup improves the performance of algorithm from O(N^2) to O(N), where N = |postorder|
        lookup = {}
        for i in range(len(inorder)):
            lookup[inorder[i]] = i 
        return self.buildTreeRecur(lookup, inorder, postorder, 0, len(postorder) - 1, len(postorder) - 1)
        
    def buildTreeRecur(self, lookup, inorder, postorder, in_start, in_end, post_end):
        if in_start > in_end:
            return None
        current = TreeNode(postorder[post_end])
        i = lookup[postorder[post_end]]
        current.left = self.buildTreeRecur(lookup, inorder, postorder, in_start, i - 1, post_end - (in_end - i) - 1)
        current.right = self.buildTreeRecur(lookup, inorder, postorder, i + 1, in_end, post_end - 1)
        return current