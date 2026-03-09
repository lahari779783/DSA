"""
Next Greater Element I

Problem:
Find next greater element of each element in nums1 using nums2.

Approach:
Use monotonic decreasing stack on nums2.
Map each number to its next greater number.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def next_greater_element(nums1, nums2):
    stack = []
    mapping = {}

    for num in nums2:
        while stack and num > stack[-1]:
            mapping[stack.pop()] = num
        stack.append(num)

    for num in stack:
        mapping[num] = -1

    result = []
    for num in nums1:
        result.append(mapping[num])

    return result


if __name__ == "__main__":
    print(next_greater_element([4,1,2], [1,3,4,2]))