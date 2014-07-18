class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        current = dummy
        heap = []
        for sorted_list in lists:
            if sorted_list:
                heapq.heappush(heap, (sorted_list.val, sorted_list))
        while heap:
            smallest = heapq.heappop(heap)[1]
            current.next = smallest
            current = current.next
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, smallest.next))
        return dummy.next