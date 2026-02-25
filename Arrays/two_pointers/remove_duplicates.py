"""
Remove Duplicates from Sorted Array

Problem:
Remove duplicates in-place and return count of unique elements.

Approach:
- Use slow pointer to store unique elements
- Compare current with previous element

Time Complexity: O(n)
Space Complexity: O(1)
"""

def remove_duplicates(nums):
    if not nums:
        return 0

    slow = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[slow] = nums[i]
            slow += 1

    return slow


if __name__ == "__main__":
    nums = [1,1,2,2,3]
    k = remove_duplicates(nums)
    print(k, nums[:k])