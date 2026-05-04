"""
Maximum Depth of Binary Tree

Problem:
Return the maximum depth of a binary tree.

Approach:
Use recursion:
depth = 1 + max(left_depth, right_depth)

Time Complexity: O(n)
Space Complexity: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    if not root:
        return 0

    left = max_depth(root.left)
    right = max_depth(root.right)

    return 1 + max(left, right)


# -------- Test --------
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(max_depth(root))  # 3