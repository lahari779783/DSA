"""
Subarray Product Less Than K

Problem:
Given an array nums and integer k,
return number of contiguous subarrays where
product of all elements < k.

Example:
nums = [10,5,2,6], k = 100
Output: 8

Approach:
Use sliding window.
Expand right pointer and shrink left pointer
when product >= k.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def num_subarray_product_less_than_k(nums, k):
    if k <= 1:
        return 0

    product = 1
    left = 0
    count = 0

    for right in range(len(nums)):
        product *= nums[right]

        while product >= k:
            product //= nums[left]
            left += 1

        count += right - left + 1

    return count


if __name__ == "__main__":
    print(num_subarray_product_less_than_k([10,5,2,6], 100))