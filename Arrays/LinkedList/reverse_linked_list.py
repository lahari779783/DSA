"""
Reverse Linked List

Problem:
Reverse a singly linked list.

Approach:
Use three pointers:
prev, curr, next_node
Reverse the direction of links one by one.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next   # store next
        curr.next = prev        # reverse link
        prev = curr             # move prev
        curr = next_node        # move curr

    return prev


# Helper function to print list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":
    # create list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print("Original:")
    print_list(head)

    head = reverse_list(head)

    print("Reversed:")
    print_list(head)