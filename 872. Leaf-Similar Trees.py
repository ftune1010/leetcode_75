# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leafSimilar(root1, root2):
    """
    :type root1: Optional[TreeNode]
    :type root2: Optional[TreeNode]
    :rtype: bool
    """
    def findLeafNodes(root):
        if not root:
            return
        if not root.left and not root.right:
            return [root.val]
        return findLeafNodes(root.left) + findLeafNodes(root.right)
    return findLeafNodes(root1) == findLeafNodes(root2)