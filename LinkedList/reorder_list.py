"""
Reorder Linked List

Problem:
Reorder a linked list as:
L0 → Ln → L1 → Ln-1 → ...

Approach:
1. Find middle using fast/slow pointers
2. Reverse second half
3. Merge both halves alternately

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head):
    if not head or not head.next:
        return

    # -------- Step 1: Find middle --------
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # -------- Step 2: Reverse second half --------
    prev = None
    curr = slow.next
    slow.next = None   # break list

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # prev is head of reversed second half

    # -------- Step 3: Merge two halves --------
    first = head
    second = prev

    while second:
        temp1 = first.next
        temp2 = second.next

        first.next = second
        second.next = temp1

        first = temp1
        second = temp2


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
    reorder_list(head)
    print_list(head)