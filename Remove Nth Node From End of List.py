class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head
        left, right = dummy, dummy
        while n:
            right, n = right.next, n-1
        while right.next: 
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next
