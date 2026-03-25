"""
Find Peak Element

Problem:
Find an index of a peak element.

Approach:
Use binary search.
Compare mid with mid+1 to decide direction.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def find_peak_element(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1   # go right
        else:
            right = mid      # keep mid

    return left


if __name__ == "__main__":
    nums = [1,2,3,1]
    print(find_peak_element(nums))