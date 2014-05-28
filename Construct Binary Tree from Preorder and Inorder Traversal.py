class Solution:
    def buildTree(self, preorder, inorder):
        # using dictionary for index lookup improves the performance of algorithm from O(N^2) to O(N), where N = |preorder|
        lookup = {}
        for i in range(len(inorder)):
            lookup[inorder[i]] = i 
        return self.buildTreeRecur(lookup, preorder, inorder, 0, len(preorder) - 1, 0)
        
    def buildTreeRecur(self, lookup, preorder, inorder, in_start, in_end, pre_start):
        if in_start > in_end:
            return None
        current = TreeNode(preorder[pre_start])
        i = lookup[preorder[pre_start]]
        current.left = self.buildTreeRecur(lookup, preorder, inorder, in_start, i - 1, pre_start + 1)
        current.right = self.buildTreeRecur(lookup, preorder, inorder, i + 1, in_end, pre_start + i - in_start + 1)
        return current