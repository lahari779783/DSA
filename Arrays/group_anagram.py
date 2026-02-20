"""Group Anagrams 

Problem
Given an array of strings strs,
group the anagrams together.

You can return the answer in any order.

Example

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]] 

Approach:
1)Create a dictionary to store the groups of anagrams.  
2)Iterate through each string in the input array:
    a) For each string, sort the characters to create a key that represents the anagram group.
    b) If the key does not exist in the dictionary, create a new entry with an empty list.
    c) Append the original string to the list corresponding to the sorted key in the dictionary.
3) Return the values of the dictionary, which will be the grouped anagrams.

Time Complexity: O(n * k log k) - We traverse the list of strings once, and for each string, we sort it which takes O(k log k) time, where k is the length of the string.
Space Complexity: O(n) - In the worst case, all strings are anagrams of each other, and we store all of them in the dictionary.

"""

def group_anagrams(strs):
    groups = {}

    for word in strs:
        key = ''.join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(group_anagrams(strs))