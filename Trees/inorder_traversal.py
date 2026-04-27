"""
Binary Tree Inorder Traversal

Problem:
Return inorder traversal of binary tree.

Approach:
LEFT → ROOT → RIGHT using recursion.

Time Complexity: O(n)
Space Complexity: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root):
    result = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print(inorder_traversal(root))