# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        """
        这一题首先就是给的反的，直接从前往后遍历

        整除 //10 取余 %10
        """


        dummy_node = ListNode(-1)
        curr = dummy_node

        p1, p2, carry = l1, l2, 0

        while p1 or p2 or carry:
            if p1:
                carry += p1.val
                p1 = p1.next
            if p2:
                carry += p2.val
                p2 = p2.next
            
            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry //= 10
        
        return dummy_node.next