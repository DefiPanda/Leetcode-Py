class Solution:
    def connect(self, root):
        if root is None:
            return
        if root.left:
            root.left.next = root.right
        if root.right and root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)