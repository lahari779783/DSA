"""
Maximum Average Subarray I

Problem:
Given an array nums and integer k,
find the maximum average value of any subarray of length k.

Example:
nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75

Approach:
Use sliding window of fixed size k.
Update window sum by removing left element and adding right.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def find_max_average(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i-k]
        max_sum = max(max_sum, window_sum)

    return max_sum / k


if __name__ == "__main__":
    print(find_max_average([1,12,-5,-6,50,3], 4))