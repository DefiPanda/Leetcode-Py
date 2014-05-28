class Solution:
    head = None
    def sortedListToBST(self, head):
        current, length = head, 0
        while current != None:
            current, length = current.next, length + 1
        self.head = head
        return self.sortedRecur(0, length - 1)
        
    def sortedRecur(self, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        left = self.sortedRecur(start, mid - 1)
        current = TreeNode(self.head.val)
        current.left = left
        self.head = self.head.next
        current.right = self.sortedRecur(mid + 1, end)
        return current