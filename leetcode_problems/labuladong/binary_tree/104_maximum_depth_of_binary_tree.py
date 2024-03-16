# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # recursive way

        """
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        """

        # traverse
        self.depth = 0
        self.result = 0

        def traverse(node):
            if not node:
                return
            
            self.depth += 1
            self.result = max(self.result, self.depth)
            traverse(node.left)
            traverse(node.right)
            self.depth -= 1
        
        traverse(root)
        
        return self.result 
    
        