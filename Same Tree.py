class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)