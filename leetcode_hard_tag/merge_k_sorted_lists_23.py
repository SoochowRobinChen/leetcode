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
            if lists[i]:
                heappush(min_heap, (lists[i].val, i, lists[i]))
        

        while min_heap:
            _, i, node = heappop(min_heap)
            p.next = node
            p = node

            if node.next:
                heappush(min_heap, (node.next.val, i, node.next))
        
        p.next = None

        return dummy_node.next 