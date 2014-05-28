class Solution:
    def hasCycle(self, head):
        fast, slow = head, head
        while(fast != None and fast.next != None):
            fast, slow = fast.next.next, slow.next
            if(fast == slow):
                return True
        return False