"""
Koko Eating Bananas

Problem:
Find minimum eating speed k such that Koko can finish all piles within h hours.

Approach:
Binary search on answer (k).
Check if a given k is valid by calculating total hours.

Time Complexity: O(n log m)
n = number of piles
m = max(piles)

Space Complexity: O(1)
"""

def min_eating_speed(piles, h):
    left = 1
    right = max(piles)

    while left < right:
        mid = (left + right) // 2

        hours = 0
        for pile in piles:
            hours += (pile + mid - 1) // mid   # ceil division

        if hours <= h:
            right = mid   # try smaller speed
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    piles = [3,6,7,11]
    h = 8
    print(min_eating_speed(piles, h))