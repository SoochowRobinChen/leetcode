# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        self.res = 0
        # kind of bottom up solution 
        def dfs(node):
            if not node:
                return []
            
            if not node.left and not node.right:
                return [1]
            
            left_sub = dfs(node.left)
            right_sub = dfs(node.right)

            for i in left_sub:
                for j in right_sub:
                    if i + j <= distance:
                        self.res += 1
            
            all_sub = left_sub + right_sub
            return [d + 1 for d in all_sub]
        
        dfs(root)

        return self.res 

        """
        这一题还可以用图来做，recursively build a graph by using adjcency list and 
        from each leaf node traverse if it can reach another each node
        """