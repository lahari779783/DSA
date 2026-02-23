"""
Running Sum of 1D Array

Problem:
Given an array nums,
return the running sum of nums.

Approach:
- Maintain a running total
- Add each element to the running total
- Store the result in a new list

Time Complexity: O(n)
Space Complexity: O(n)
"""

def running_sum(nums):
    result = []
    current_sum = 0

    for num in nums:
        current_sum += num
        result.append(current_sum)

    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(running_sum(nums))  