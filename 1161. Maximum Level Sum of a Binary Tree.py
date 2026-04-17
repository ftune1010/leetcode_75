class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxLevelSum(self, root: TreeNode) -> int:
    # BFS
    # from collections import deque

    # if not root:
    #     return 1

    # que = deque([root])
    # max_sum = float("-inf")
    # max_level = curr_level = 0

    # while que:
    #     curr_sum = 0
    #     curr_level += 1
    #     for _ in range(len(que)):
    #         node = que.popleft()
    #         curr_sum += node.val
    #         if node.left:
    #             que.append(node.left)
    #         if node.right:
    #             que.append(node.right)
    #     if curr_sum > max_sum:
    #         max_sum = curr_sum
    #         max_level = curr_level
    # return max_level 

    #DFS

    from collections import defaultdict

    levels = defaultdict(int)
    
    def dfs(node: TreeNode, level: int) -> None:
        if node:
            levels[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
    
    dfs(root, 1)

    return max(levels, key=levels.get)


            

    