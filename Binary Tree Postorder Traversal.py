class Solution:
    def postorderTraversal(self, root):
        result = []
        self.recur(root, result)
        return result
    
    def recur(self, root, result):
        if(root == None):
            return
        self.recur(root.left, result)
        self.recur(root.right, result)
        result.append(root.val)