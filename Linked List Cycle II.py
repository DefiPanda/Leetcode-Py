class Solution:
    def detectCycle(self, head):
        fast, slow = head, head
        while fast != None and fast.next != None:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                fast = head
                while fast != slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None