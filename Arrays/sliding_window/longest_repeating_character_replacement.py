"""
Longest Repeating Character Replacement

Problem:
Given a string s and integer k,
return the length of the longest substring
containing the same letter after replacing
at most k characters.

Approach:
Use sliding window and frequency count.
Track the most frequent character in the window.
Shrink window if replacements exceed k.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def character_replacement(s, k):
    count = {}
    left = 0
    max_freq = 0
    max_length = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_freq = max(max_freq, count[s[right]])

        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    print(character_replacement("AABABBA", 1))  # Output: 4