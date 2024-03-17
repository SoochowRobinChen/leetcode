# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root: return None

        if root.val == key:
            if not root.left: return root.right
            if not root.right: return root.left

            min_node = self.getMin(root.right)
            root.right = self.deleteNode(root.right, min_node.val)

            min_node.left = root.left
            min_node.right = root.right
            root = min_node

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        return root
        
    def getMin(self, node):
            curr = node
            while curr.left:
                curr = curr.left
            return curr