class Solution:
    def swapPairs(self, head):
        if head != None and head.next != None:
            next = head.next
            head.next = self.swapPairs(next.next)
            next.next = head
            return next
        return head
        
    # This is the non-recursive solution
    # def swapPairs(self, head):
    #     current = ListNode(0)
    #     current.next = head
    #     head = current
    #     while current.next != None and current.next.next != None:
    #         next = current.next
    #         next_three = next.next.next
    #         current.next = next.next
    #         current.next.next = next
    #         next.next = next_three
    #         current = next
    #     return head.next