class Solution:
    def copyRandomList(self, head):
        dummy = RandomListNode(0)
        current, prev = head, dummy
        map = {}
        while current != None:
            current_copy = RandomListNode(current.label)
            prev.next = current_copy
            map[current] = current_copy
            prev = current_copy
            current = current.next
        current = head
        while current != None:
            if current.random != None:
                map[current].random = map[current.random]
            current = current.next
        return dummy.next