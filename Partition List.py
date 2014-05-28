class Solution:
    def partition(self, head, x):
        smaller, larger = ListNode(0), ListNode(0)
        smaller_copy, larger_copy = smaller, larger
        while head != None:
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
            else:
                larger.next = head
                larger = larger.next
            head = head.next
        smaller.next = larger_copy.next
        larger.next = None
        return smaller_copy.next