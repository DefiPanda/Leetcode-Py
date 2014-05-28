class Solution:
    def preorderTraversal(self, root):
        result = []
        self.recur(root, result)
        return result
    
    def recur(self, root, result):
        if(root == None):
            return
        result.append(root.val)
        self.recur(root.left, result)
        self.recur(root.right, result)