"""Valid Anagram
Problem

Given two strings s and t,
return True if t is an anagram of s,
otherwise return False.

Approach:
1)Create an empty dictionary to store the frequency of characters in string s.          
2)Iterate through the characters in string s and update the frequency in the dictionary.
3)Iterate through the characters in string t and check if they exist in the dictionary.
    a) If a character does not exist in the dictionary, return False.
    b) If a character exists, decrement its frequency in the dictionary. If the frequency becomes negative, return False.
4)If we successfully iterate through string t without returning False, return True.

Time Complexity: O(n) - We traverse both strings once.
Space Complexity: O(1) - The dictionary will have at most 26 entries for lowercase"""

def valid_anagram(s,t):
    freq={}
    if len(s)!=len(t):
        return False
    else:
        for char in s:
            freq[char]=freq.get(char,0)+1
        for char in t:
            if char not in freq:
                return False
            freq[char]-=1
            if freq[char]<0:
                return False    
    return True

if __name__=="__main__":
    s="rat"
    t="car"
    print(valid_anagram(s,t))