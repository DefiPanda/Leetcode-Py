class Solution:
    def rotateRight(self, head, k):
        if head is None:
            return None
        copy, length = head, 1
        while copy.next:
            copy, length = copy.next, length + 1
        copy.next = head
        k = length - k % length - 1
        while k > 0:
            head, k = head.next, k - 1
        tmp = head.next
        head.next = None
        return tmp