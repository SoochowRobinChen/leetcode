# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        # nested function
        def checkLeaf(root, ans):
            if not root:
                return
            
            checkLeaf(root.left, ans)

            if not root.left and not root.right:
                ans.append(root.val)
            
            checkLeaf(root.right, ans)

        # two variables
        ans1, ans2 = [], []

        checkLeaf(root1, ans1)
        checkLeaf(root2, ans2)

        return ans1 == ans2
    
        