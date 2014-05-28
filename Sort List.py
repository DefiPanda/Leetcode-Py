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
        
    def sortList(self, head):
        if head == None or head.next == None:
            return head
        fast, slow, prev = head, head, None
        while fast != None and fast.next != None:
            prev, fast, slow = slow, fast.next.next, slow.next
        prev.next = None
        sorted_l1 = self.sortList(head)
        sorted_l2 = self.sortList(slow)
        return self.mergeTwoLists(sorted_l1, sorted_l2)