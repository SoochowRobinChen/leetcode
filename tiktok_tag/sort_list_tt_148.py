# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use min_heap to sort the list
        min_heap = []

        p = head
        dummy_node = ListNode(-1)
        index = 0

        while p:
            heappush(min_heap, (p.val, index, p))
            p = p.next
            index += 1
        
        p = dummy_node
        while min_heap:
            _, _, curr_node = heappop(min_heap)
            p.next = curr_node
            p = p.next
        
        # remember to set p.next = None to avoid cycle 
        p.next = None
        return dummy_node.next 