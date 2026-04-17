class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longestZigZag(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    self.path = 0

    def zigZag(node, left, count):
        if not node:
            return
        if self.path < count:
            self.path = count
        if left:
            zigZag(node.right, False, count + 1)
            zigZag(node.left, True, 1)
        else:
            zigZag(node.left, True, count + 1)
            zigZag(node.right, False, 1)
        
    zigZag(root.left, True, 1)
    zigZag(root.right, False, 1)
    return self.path