"""#1)Two Sum
Problem

Given an array of integers nums and an integer target,
return the indices of the two numbers such that they add up to target.


Approach:
1. Create an empty dictionary to store the indices of the numbers.
2. Iterate through the array of integers.   
    a. For each number, calculate the value needed to reach the target by subtracting the current number from the target.
    b. Check if this value exists in the dictionary. If it does, return the indices of the current number and the number found in the dictionary.
    c. If it does not exist, add the current number and its index to the dictionary.
 
    
Time Complexity: O(n) - We traverse the list of numbers once.
Space Complexity: O(n) - In the worst case, we might store all numbers in the dictionary.
"""


def two_sum(nums,target):
    seen={}
    for i,num in enumerate(nums):
        complement=target-num
        if complement in seen:
            return [seen[complement],i]
        seen[num]=i
    return []

if __name__ =="__main__":
    nums=[2,7,11,15]
    target=9
    print(two_sum(nums,target))