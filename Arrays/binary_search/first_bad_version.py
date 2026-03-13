"""
First Bad Version

Problem:
Find the first bad version among n versions.

Approach:
Use binary search to minimize API calls.
If mid version is bad, search left side.
Otherwise search right side.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

# Example API simulation
def isBadVersion(version):
    BAD_VERSION = 4
    return version >= BAD_VERSION


def first_bad_version(n):
    left = 1
    right = n

    while left < right:
        mid = (left + right) // 2

        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    n = 5
    print(first_bad_version(n))