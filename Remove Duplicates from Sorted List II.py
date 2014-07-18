class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next:
            next = current.next
            while next.next and next.next.val == next.val:
                next = next.next
            if current.next is not next:
                current.next = next.next
            else:
                current = current.next
        return dummy.next