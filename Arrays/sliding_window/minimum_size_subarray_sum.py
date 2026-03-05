"""
Minimum Size Subarray Sum

Problem:
Given an array nums and a target value,
return the minimal length of a subarray
whose sum is >= target.

Approach:
Use sliding window.
Expand window by moving right pointer.
Shrink window from left while sum >= target.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def min_subarray_len(target, nums):
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return 0 if min_length == float('inf') else min_length


if __name__ == "__main__":
    print(min_subarray_len(7, [2,3,1,2,4,3]))  # Output: 2