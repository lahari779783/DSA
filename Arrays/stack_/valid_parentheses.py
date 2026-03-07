"""
Valid Parentheses

Problem:
Check if the given string of brackets is valid.

Approach:
Use a stack to track opening brackets.
Match them with closing brackets.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def is_valid(s):
    stack = []
    
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return len(stack) == 0


if __name__ == "__main__":
    print(is_valid("()[]{}"))