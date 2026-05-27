"""
Diameter of Binary Tree

Problem:
Return the diameter (longest path) of a binary tree.

Approach:
For every node:
diameter = left_height + right_height

Use DFS to calculate heights while updating maximum diameter.

Time Complexity: O(n)
Space Complexity: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root):
    diameter = 0

    def dfs(node):
        nonlocal diameter

        if not node:
            return 0

        left_height = dfs(node.left)
        right_height = dfs(node.right)

        # update diameter
        diameter = max(diameter, left_height + right_height)

        # return height
        return 1 + max(left_height, right_height)

    dfs(root)

    return diameter


# -------- Test --------
if __name__ == "__main__":
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(diameter_of_binary_tree(root))  # 3