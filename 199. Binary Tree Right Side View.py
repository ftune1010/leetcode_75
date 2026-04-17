class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: TreeNode) -> list[int]:
    # BFS
    # from collections import deque

    if not root:
        return []
    
    # res = []
    # que = deque([root])

    # while que:
    #     for i in range(len(que)):
    #         node = que.popleft()
    #         if node.left:
    #             que.append(node.left)
    #         if node.right:
    #             que.append(node.right)
    #     res.append(node.val)
    # return res

    #DFS
    res = []
    def dfs(node: TreeNode, level: int) -> None:
        if not node:
            return
        if level == len(res):
            res.append(node.val)
        dfs(node.right, level + 1)
        dfs(node.left, level + 1)
        
    dfs(root, 0)
    return res