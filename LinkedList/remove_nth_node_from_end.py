"""
Remove Nth Node From End

Problem:
Remove the nth node from the end of a linked list.

Approach:
Use two pointers (fast and slow).
Move fast n steps ahead, then move both until fast reaches end.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head

    fast = dummy
    slow = dummy

    # Move fast n steps ahead
    for _ in range(n):
        fast = fast.next

    # Move both pointers
    while fast.next:
        fast = fast.next
        slow = slow.next

    # Remove nth node
    slow.next = slow.next.next

    return dummy.next


# -------- Helper functions --------

def build_list(arr):
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# -------- Test --------

if __name__ == "__main__":
    head = build_list([1,2,3,4,5])
    head = remove_nth_from_end(head, 2)
    print_list(head)