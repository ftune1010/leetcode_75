class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deleteNode(root: TreeNode, key: int) -> TreeNode:

    def delete(root: TreeNode) -> TreeNode:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        node = root
        left = root.left
        right = root.right
        
        while left.right:
            left = left.right
        left.right = right
        return node.left
    
    if not root:
        return None
    if root.val == key:
        return delete(root)
    
    node = root
    while node:
        if key < node.val:
            if node.left and node.left.val == key:
                node.left = delete(node.left)
                break
            node = node.left
        else:
            if node.right and node.right.val == key:
                node.right = delete(node.right)
                break
            node = node.right
    return root