"""
Permutation in String

Problem:
Given two strings s1 and s2, return True if s2 contains
a permutation of s1.

Example:
s1 = "ab"
s2 = "eidbaooo"
Output: True

Approach:
Use sliding window with frequency dictionaries.
Compare the frequency of characters in window of s2 with s1.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def check_inclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    count1 = {}
    count2 = {}

    for c in s1:
        count1[c] = count1.get(c, 0) + 1

    left = 0

    for right in range(len(s2)):
        count2[s2[right]] = count2.get(s2[right], 0) + 1

        if right - left + 1 > len(s1):
            count2[s2[left]] -= 1
            if count2[s2[left]] == 0:
                del count2[s2[left]]
            left += 1

        if count1 == count2:
            return True

    return False


if __name__ == "__main__":
    print(check_inclusion("ab", "eidbaooo"))