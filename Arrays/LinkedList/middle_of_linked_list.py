"""
Middle of Linked List

Problem:
Find the middle node of a linked list.
If even length, return second middle.

Approach:
Use slow and fast pointers.
Slow moves 1 step, fast moves 2 steps.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# Helper functions
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


if __name__ == "__main__":
    head = build_list([1,2,3,4,5,6])
    mid = middle_node(head)
    print("Middle:", mid.val)