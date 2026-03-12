"""
Largest Rectangle in Histogram

Problem:
Given an array of bar heights, return the area of the largest rectangle
that can be formed in the histogram.

Approach:
Use a monotonic increasing stack.
When a smaller bar appears, compute areas for taller bars.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)   # sentinel to empty stack

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]

            if stack:
                width = i - stack[-1] - 1
            else:
                width = i

            max_area = max(max_area, height * width)

        stack.append(i)

    return max_area


if __name__ == "__main__":
    heights = [2,1,5,6,2,3]
    print(largest_rectangle_area(heights))