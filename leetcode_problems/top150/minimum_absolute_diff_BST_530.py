# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev_node = None
        self.min_value = float('inf')

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            if self.prev_node:
                self.min_value = min(self.min_value, node.val - self.prev_node.val)
            
            self.prev_node = node

            inorder(node.right)
        
        inorder(root)

        return self.min_value