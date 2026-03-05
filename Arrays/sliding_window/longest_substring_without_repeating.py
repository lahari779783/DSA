"""
Longest Substring Without Repeating Characters

Problem:
Given a string s, find the length of the longest substring
without repeating characters.

Approach:
Use sliding window with a set to track characters.
Expand right pointer and shrink left pointer when duplicates appear.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    print(longest_substring("abcabcbb"))  # Output: 3