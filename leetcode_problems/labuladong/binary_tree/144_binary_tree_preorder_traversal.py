# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #  use nested function

        """
        results = []

        def traverse(node):
            if not node:
                return 
            
            results.append(node.val)
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return results
        """

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []
    
        
    
    