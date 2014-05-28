class Solution:
    def isBalanced(self, root):
        return self.getHeight(root) != -1
    
    def getHeight(self, root):
        if root == None:
            return 0
        left_height, right_height = self.getHeight(root.left), self.getHeight(root.right) 
        if left_height < 0 or right_height < 0 or math.fabs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1