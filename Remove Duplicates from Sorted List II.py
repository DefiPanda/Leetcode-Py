class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        head, current = dummy, dummy
        while current.next != None:
            next = current.next
            while next.next != None and next.next.val == next.val:
                next = next.next
            if next != current.next:
                current.next = next.next
            else:
                current = current.next
        return head.next