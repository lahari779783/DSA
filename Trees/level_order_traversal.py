"""
Binary Tree Level Order Traversal

Problem:
Return level order traversal of a binary tree.

Approach:
Use BFS with a queue.
Process nodes level by level.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


# -------- Test --------
if __name__ == "__main__":
    # Tree:
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(level_order(root))  # [[3], [9,20], [15,7]]