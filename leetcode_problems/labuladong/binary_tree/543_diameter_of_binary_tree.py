# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def traverse(node):
            if not node:
                return 0
            
            left_max = traverse(node.left)
            right_max = traverse(node.right)
            
            self.result = max(self.result, left_max + right_max)

            return max(left_max, right_max) + 1
        
        traverse(root)

        return self.result