"""
Same Tree

Problem:
Check if two binary trees are identical.

Approach:
Use recursion:
- Compare current nodes
- Recursively check left and right subtrees

Time Complexity: O(n)
Space Complexity: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):
    # both null → identical
    if not p and not q:
        return True

    # one null → not identical
    if not p or not q:
        return False

    # values different → not identical
    if p.val != q.val:
        return False

    # check subtrees
    return (
        is_same_tree(p.left, q.left) and
        is_same_tree(p.right, q.right)
    )


# -------- Test --------
if __name__ == "__main__":
    # Tree p: 1 → 2 → 3
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    # Tree q: 1 → 2 → 3
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    print(is_same_tree(p, q))  # True