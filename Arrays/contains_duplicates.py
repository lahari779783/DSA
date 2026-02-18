""" Contains Duplicate
Problem
Given an integer array nums,
return True if any value appears at least twice,
and False if every element is distinct.


Approach:
1)create an empty set to store the unique numbers.
2)Iterate through the array of integers
3)For each number , check if it already exits in the set.If it does return true.
4)If it does not exist, add the number to the set.

Time Complexity: O(n) - We traverse the list of numbers once.
Space Complexity: O(n) - In the worst case, we might store all numbers in the set.

"""


def contains_duplicate(nums):
    seen=set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__=="__main__":
    nums=[1,2,3,1]
    print(contains_duplicate(nums))
