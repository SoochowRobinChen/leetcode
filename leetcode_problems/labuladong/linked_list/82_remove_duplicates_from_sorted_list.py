# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = dummy
        q = head

        while q:
            if q.next and q.val == q.next.val:
                while q.next and q.val == q.next.val:
                    q = q.next
                q = q.next
                if not q:
                    p.next = None
            else:
                p.next = q
                p = p.next
                q = q.next
        
        return dummy.next 