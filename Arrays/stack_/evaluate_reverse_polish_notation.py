"""
Evaluate Reverse Polish Notation

Problem:
Evaluate an arithmetic expression given in Reverse Polish Notation.

Approach:
Use a stack to store numbers.
When an operator appears, pop the top two numbers,
apply the operation, and push the result back.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def eval_rpn(tokens):
    stack = []

    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)

            elif token == "-":
                stack.append(a - b)

            elif token == "*":
                stack.append(a * b)

            else:
                stack.append(int(a / b))  # integer division

        else:
            stack.append(int(token))

    return stack[0]


if __name__ == "__main__":
    tokens = ["2","1","+","3","*"]
    print(eval_rpn(tokens))