class Solution:
    def copyRandomList(self, head):
        dummy = RandomListNode(0)
        current, prev, map = head, dummy, {}
        while current:
            copy = RandomListNode(current.label)
            map[current] = copy
            prev.next = copy
            prev, current = prev.next, current.next
        current = head
        while current:
            if current.random:
                map[current].random = map[current.random]
            current = current.next
        return dummy.next