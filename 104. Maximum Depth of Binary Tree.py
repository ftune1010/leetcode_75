# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    # DFS Solution
    # if root is None:
    #     return 0
    # return 1 + max(maxDepth(root.left), maxDepth(root.right))

    # BFS: More Efficient for this problem
    from collections import deque
    
    if not root:
        return 0

    q = deque()
    q.append(root)
    depth = 0
    while q:
        depth += 1

        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return depth