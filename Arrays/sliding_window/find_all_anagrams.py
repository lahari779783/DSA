"""
Find All Anagrams in a String

Problem:
Given strings s and p,
return all start indices of p's anagrams in s.

Example:
s = "cbaebabacd"
p = "abc"

Output: [0,6]

Approach:
Use sliding window with frequency dictionaries.
Window size equals length of p.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def find_anagrams(s, p):
    result = []
    p_count = {}
    window = {}

    for c in p:
        p_count[c] = p_count.get(c, 0) + 1

    left = 0

    for right in range(len(s)):
        window[s[right]] = window.get(s[right], 0) + 1

        if right - left + 1 > len(p):
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1

        if window == p_count:
            result.append(left)

    return result


if __name__ == "__main__":
    print(find_anagrams("cbaebabacd", "abc"))