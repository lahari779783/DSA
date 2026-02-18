"""Intersection of Two Arrays
Problem

Given two integer arrays nums1 and nums2,
return an array of their intersection.

Each element in the result must be unique.
Order does not matter.


Approach:
1)Convert both arrays into sets to get unique elements.
2)Use the set intersection operation to find common elements between the two sets.  
3)Convert the resulting set back into a list and return it.


Time Complexity: O(n + m) - We traverse both arrays once to create the sets, where n and m are the lengths of nums1 and nums2 respectively. The intersection operation takes O(min(n, m)).
Space Complexity: O(n + m) - In the worst case, we might store all unique"""

def intersection(num1,num2):
    set1=set(num1)
    set2=set(num2)
    return list(set1 & set2)

if __name__=="__main__":
    num1=[1,2,2,1]
    num2=[2,2,1]
    print(intersection(num1,num2))