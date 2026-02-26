"""
Two Sum II - Sorted Array

Time Complexity: O(n)
Space Complexity: O(1)
"""

def two_sum_sorted(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1


if __name__ == "__main__":
    print(two_sum_sorted([2,7,11,15], 9))