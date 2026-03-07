"""
Min Stack

Problem:
Design a stack that supports push, pop, top,
and retrieving the minimum element in constant time.

Approach:
Use two stacks:
1. main stack
2. min stack to track minimum values

Time Complexity: O(1)
Space Complexity: O(n)
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


if __name__ == "__main__":
    obj = MinStack()

    obj.push(5)
    obj.push(3)
    obj.push(7)

    print(obj.getMin())  # 3