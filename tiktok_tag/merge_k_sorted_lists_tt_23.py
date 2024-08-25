# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_node = ListNode(-1)
        p = dummy_node
        min_heap = []

        for i in range(len(lists)):
            node = lists[i]
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        while min_heap:
            _, i, node = heapq.heappop(min_heap)

            p.next = node
            p = p.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy_node.next 
        