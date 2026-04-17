class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def isGood(node, max_val):
        if not node:
            return 0
        if node.val < max_val:
            return isGood(node.left, max_val) + isGood(node.right, max_val)
        if node.val > max_val:
            max_val = node.val
        return 1 + isGood(node.left, max_val) + isGood(node.right, max_val)
    return isGood(root, root.val)


if __name__ == "__main__":
    A = TreeNode(3)
    B = TreeNode(1)
    C = TreeNode(4)
    D = TreeNode(3)
    E = TreeNode(1)
    F = TreeNode(5)

    A.left = B
    A.right = C
    B.left = D
    C.left = E
    C.right = F

    print(goodNodes(A))