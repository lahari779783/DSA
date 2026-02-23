"""
Maximum Subarray

Problem:
Given an integer array nums,
find the contiguous subarray with the largest sum and return the sum.

Approach (Kadane's Algorithm):
- Maintain current_sum = max subarray ending at current index
- Maintain max_sum = maximum subarray sum seen so far
- At each step, decide whether to extend previous subarray or start new

Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(max_subarray(nums))  