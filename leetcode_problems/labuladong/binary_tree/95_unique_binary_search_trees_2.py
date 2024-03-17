# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def generate(l, r):
            res = []
            if l > r:
                return [None]
            
            for i in range(l, r+1):
                left_subtree = generate(l, i - 1)
                right_subtree = generate(i + 1, r)

                for left in left_subtree:
                    for right in right_subtree:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right

                        res.append(root)
            
            return res
        
        return generate(1, n)