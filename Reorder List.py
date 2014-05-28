class Solution:
    def reorderList(self, head):
        if head == None or head.next == None:
            return head
        fast, slow, prev = head, head, None
        while fast != None and fast.next != None:
            fast, slow, prev = fast.next.next, slow.next, slow
        current, prev.next, prev = slow, None, None
        while current != None:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        l1, l2 = head, prev
        current = l1
        while l1 != None and l2 != None:
            current.next, current, l1 = l1, l1, l1.next
            current.next, current, l2 = l2, l2, l2.next
        return head