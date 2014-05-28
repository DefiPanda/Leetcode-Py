class Solution:
    def connect(self, root):
        if root == None:
            return root
        current = [root]
        while len(current) > 0:
            next = []
            for i in range(len(current)):
                this_node = current[i]
                if i < len(current) - 1:
                    this_node.next = current[i+1]
                if this_node.left != None:
                    next.append(this_node.left)
                if this_node.right != None:
                    next.append(this_node.right)
            current = next