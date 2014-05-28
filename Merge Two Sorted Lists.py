class Solution:
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        current = head
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                current.next, current, l1 = l1, l1, l1.next
            else:
                current.next, current, l2 = l2, l2, l2.next
        if l1 != None:
            current.next = l1
        if l2 != None:
            current.next = l2
        return head.next