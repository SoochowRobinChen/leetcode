# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_list, greater_list = ListNode(-1), ListNode(-1)
        p1, p2, p = smaller_list, greater_list, head

        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            
            p = p.next 
        
        # p2.next = None
        p2.next = None

        p1.next = greater_list.next

        return smaller_list.next 