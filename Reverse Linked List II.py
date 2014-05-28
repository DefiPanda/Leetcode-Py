class Solution:
    def reverseBetween(self, head, m, n):
        diff, dummy, current= n - m, ListNode(0), head
        dummy.next = head
        last_unswapped = dummy
        while current != None and m > 1:
            current, last_unswapped, m = current.next, current, m - 1
        prev, first_swapped = last_unswapped, current
        while current != None and diff >= 0:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
            diff -= 1
        last_unswapped.next, first_swapped.next = prev, current
        return dummy.next