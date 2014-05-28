class Solution:
    def rotateRight(self, head, n):
        if head == None:
            return None
        current, length = head, 1
        while current.next != None:
            current, length = current.next, length + 1
        current.next = head
        n = length - n % length
        while n > 0:
            current, n = current.next, n - 1
        head = current.next
        current.next = None
        return head