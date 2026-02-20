"""First Unique Character in a String

Problem
Given a string s,
find the first non-repeating character in it
and return its index.

If it does not exist, return -1.

Approach:
1)Create a dictionary to store the frequency of each character in the string.
2)Iterate through the string and update the frequency of each character in the dictionary.  
3)Iterate through the string again and check the frequency of each character in the dictionary.
    a) If the frequency is 1, return the index of that character.
4)If we finish iterating through the string without finding a non-repeating character, return -1.
Time Complexity: O(n) - We traverse the string twice.
Space Complexity: O(1) - The dictionary will have at most 26 entries for lowercase letters.

"""


def first_uniq_char(s):
    char_count = {}
    for ch in s:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1
    for i, ch in enumerate(s):
        if char_count[ch] == 1:
            return i

    return -1


if __name__ == "__main__":
    s = "leetcode"
    print(first_uniq_char(s))  # Output: 0