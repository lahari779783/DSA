"""
Next Greater Element II

Problem:
Given a circular array nums, return the next greater element
for every element.

Approach:
Use a monotonic decreasing stack.
Traverse the array twice to simulate circular behavior.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def next_greater_elements(nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(2 * n):
        while stack and nums[i % n] > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i % n]

        if i < n:
            stack.append(i)

    return result


if __name__ == "__main__":
    nums = [1,2,1]
    print(next_greater_elements(nums))