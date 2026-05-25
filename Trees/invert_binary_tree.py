"""
Invert Binary Tree

Problem:
Invert (mirror) a binary tree.

Approach:
For every node:
1. Swap left and right child
2. Recursively invert subtrees

Time Complexity: O(n)
Space Complexity: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if not root:
        return None

    # swap children
    root.left, root.right = root.right, root.left

    # recursively invert subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root


# -------- Helper --------
def level_order(root):
    from collections import deque

    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result


# -------- Test --------
if __name__ == "__main__":
    root = TreeNode(4)

    root.left = TreeNode(2)
    root.right = TreeNode(7)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    inverted = invert_tree(root)

    print(level_order(inverted))