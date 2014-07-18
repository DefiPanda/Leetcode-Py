class Solution:
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            next = current.next
            if current.val == next.val:
                current.next = current.next.next
            else:
                current = next
        return head