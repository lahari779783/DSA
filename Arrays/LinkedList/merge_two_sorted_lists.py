"""
Merge Two Sorted Lists

Problem:
Merge two sorted linked lists and return the merged list.

Approach:
Use a dummy node.
Compare nodes from both lists and build the result.

Time Complexity: O(n + m)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    # Attach remaining nodes
    if list1:
        current.next = list1
    else:
        current.next = list2

    return dummy.next


# Helper to print list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":
    # list1: 1 → 2 → 4
    l1 = ListNode(1, ListNode(2, ListNode(4)))

    # list2: 1 → 3 → 4
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    merged = merge_two_lists(l1, l2)

    print_list(merged)