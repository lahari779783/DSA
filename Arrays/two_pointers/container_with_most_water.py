"""
Container With Most Water

Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        max_water = max(max_water, width * current_height)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


if __name__ == "__main__":
    print(max_area([1,8,6,2,5,4,8,3,7]))