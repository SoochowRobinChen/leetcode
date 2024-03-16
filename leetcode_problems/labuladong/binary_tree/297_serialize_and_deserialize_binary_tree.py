# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'X'
        node = str(root.val)
        node_left = str(self.serialize(root.left))
        node_right = str(self.serialize(root.right))
        return ','.join([node, node_left, node_right])
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.data = data
        if self.data[0] == 'X':
            return None
        
        node = TreeNode(self.data[:self.data.find(',')])
        node_left = self.deserialize(self.data[self.data.find(',') + 1:])
        node_right = self.deserialize(self.data[self.data.find(',') + 1:])

        node.left, node.right = node_left, node_right

        return node
        