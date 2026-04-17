class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(self, root, targetSum):
    """
    :type root: Optional[TreeNode]
    :type targetSum: int
    :rtype: int
    """
    self.paths = 0
    cache = {0:1}
    def dfs(node, currSum, cache):
        if node is None:
            return
        currSum += node.val
        self.paths += cache.get(currSum - targetSum, 0)
        cache[currSum] = cache.get(currSum, 0) + 1
        if node.right:
            dfs(node.right, currSum, cache)
        if node.left:
            dfs(node.left, currSum, cache)
        cache[currSum] -= 1
    dfs(root, 0, cache)
    return self.paths