"""
Squares of a Sorted Array

Time Complexity: O(n)
Space Complexity: O(n)
"""

def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] ** 2
            left += 1
        else:
            result[pos] = nums[right] ** 2
            right -= 1
        pos -= 1

    return result


if __name__ == "__main__":
    print(sorted_squares([-4,-1,0,3,10]))