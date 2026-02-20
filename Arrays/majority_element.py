"""Majority Element

Problem
Given an array nums of size n,
return the element that appears more than ⌊n / 2⌋ times.

You may assume that the majority element always exists.


Approach:
1)Create an empty dictionary to store the frequency of elements in the array.
2)Iterate through the array of integers and update the frequency in the dictionary.
3)Iterate through the dictionary and check if any element has a frequency greater than n/2. If it does, return that element.


Time Complexity: O(n) - We traverse the list of numbers once and then iterate through the dictionary.
Space Complexity: O(n) - In the worst case, we might store all numbers in the dictionary.
"""

def majority_element(nums):
    count={}
    for i in nums:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for key in count:
        if count[key]>len(nums)//2:
            return key
            
    return -1

if __name__=="__main__":
    nums=[3,2,3]
    print(majority_element(nums))