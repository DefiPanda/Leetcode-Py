class Solution:
    def mergeKLists(self, lists):
        heap = []
        for list in lists:
            if list != None:
                heapq.heappush(heap, (list.val, list))
        dummy = ListNode(0)
        prev = dummy
        while len(heap) > 0:
            tmp = heapq.heappop(heap)[1]
            prev.next = tmp
            if tmp.next != None:
                heapq.heappush(heap, (tmp.next.val, tmp.next))
            prev = prev.next
        return dummy.next