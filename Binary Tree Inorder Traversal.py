class Solution:
    def inorderTraversal(self, root):
        result = []
        self.recur(root, result)
        return result
    
    def recur(self, root, result):
        if(root == None):
            return
        self.recur(root.left, result)
        result.append(root.val)
        self.recur(root.right, result)