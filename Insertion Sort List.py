class Solution:
    def insertionSortList(self, head):
        if head == None:
            return head
        dummy = ListNode(-9223372036854775808)
        dummy.next = head
        current, prev_current = head.next, head
        while current != None:
            prev = dummy
            while prev.next.val < current.val:
                prev = prev.next
            if prev.next != current and prev.next.val >= current.val:
                current.next, prev.next, prev_current.next = prev.next, current, current.next
                current = prev_current.next
            else:
                current, prev_current = current.next, prev_current.next
        return dummy.next