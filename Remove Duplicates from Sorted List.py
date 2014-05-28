class Solution:
    def deleteDuplicates(self, head):
        current = head
        while current != None:
            next = current.next
            if next != None:
                if next.val == current.val:
                    current.next = next.next
                else:
                    current = current.next
            else:
                break
        return head