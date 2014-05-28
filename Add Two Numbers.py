class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current, carry = dummy, 0
        while l1 != None or l2 != None:
            res = carry
            if l1 != None:
                res += l1.val
                l1 = l1.next
            if l2 != None:
                res += l2.val
                l2 = l2.next
            carry, res = res / 10, res % 10
            current.next = ListNode(res)
            current = current.next
        if carry == 1:
            current.next = ListNode(1)
        return dummy.next