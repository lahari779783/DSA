"""
Move Zeroes

Problem:
Move all zeroes to the end while keeping order of non-zero elements.

Approach:
- Use a pointer to place non-zero values
- Fill remaining places with zero

Time Complexity: O(n)
Space Complexity: O(1)
"""

def move_zeroes(nums):
    pos = 0

    for num in nums:
        if num != 0:
            nums[pos] = num
            pos += 1

    for i in range(pos, len(nums)):
        nums[i] = 0


if __name__ == "__main__":
    nums = [0,1,0,3,12]
    move_zeroes(nums)
    print(nums)