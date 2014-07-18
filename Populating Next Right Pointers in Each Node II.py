class Solution:
    def connect(self, root):
        if root is None:
            return root
        current = [root]
        while current:
            next = []
            for i in range(len(current)):
                if i < len(current) - 1:
                    current[i].next = current[i + 1]
                if current[i].left is not None:
                    next.append(current[i].left)
                if current[i].right is not None:
                    next.append(current[i].right)
            current = next
        return root