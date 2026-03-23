"""
Find First and Last Position of Element

Problem:
Given a sorted array nums and a target value,
find the starting and ending position of the target.

Approach:
Use binary search twice:
1. Find first occurrence
2. Find last occurrence

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def search_range(nums, target):

    def find_first():
        left, right = 0, len(nums) - 1
        first = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                first = mid
                right = mid - 1   # move left
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return first


    def find_last():
        left, right = 0, len(nums) - 1
        last = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                last = mid
                left = mid + 1   # move right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return last


    return [find_first(), find_last()]


if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    print(search_range(nums, target))