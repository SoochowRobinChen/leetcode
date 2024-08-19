# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_node = p = ListNode(-1)
        min_heap = []
        # why we need i here? it is used for sorting if node.val is equal
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        while min_heap:
            _, i, node = heapq.heappop(min_heap)

            p.next = node
            p = p.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy_node.next 