"""
Linked List Cycle (Floyd’s Algorithm)

Problem:
Check if a linked list contains a cycle.

Approach:
Use two pointers (slow and fast).
If they meet → cycle exists.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          # move 1 step
        fast = fast.next.next     # move 2 steps

        if slow == fast:
            return True

    return False


# Test case
if __name__ == "__main__":
    # Create nodes
    head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)

    # Link nodes
    head.next = second
    second.next = third
    third.next = fourth

    # Create cycle: 4 → 2
    fourth.next = second

    print(has_cycle(head))  # True