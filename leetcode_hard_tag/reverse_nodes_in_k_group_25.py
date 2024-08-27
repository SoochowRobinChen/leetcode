# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        
        a, b = head, head

        for _ in range(k):
            if not b:
                return head
            b = b.next
        
        new_head = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)

        return new_head
    
    def reverse(self, a, b):

        prev = None
        curr = a

        while curr != b:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev