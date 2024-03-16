# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        visited = defaultdict(int)
        res = []
        
        def serialize(node):
            if not node: return '#'

            left = serialize(node.left)
            right = serialize(node.right)
            # learn how to serialize a tree, to make sure it is unique
            subtree = left + ',' + right + ',' + str(node.val)
            freq = visited.get(subtree)
            if freq == 1:
                res.append(node)
            
            visited[subtree] += 1

            return subtree
        
        serialize(root)
        return res
