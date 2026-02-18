"""Longest Consecutive Sequence (Medium)
Problem

Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


Approach:
1)Create a set from the input array to allow for O(1) lookups.
2)Initialize a variable longest_streak to keep track of the longest consecutive sequence found.
3)Iterate through each number in the set:   
    a) For each number, check if it is the start of a sequence by verifying that the number one less than it does not exist in the set.
    b) If it is the start of a sequence, initialize a variable current_num to the current number and a variable current_streak to 1.
    c) While the next consecutive number (current_num + 1) exists in the set, increment current_num and current_streak.
    d) Update longest_streak with the maximum of longest_streak and current_streak.

Time Complexity: O(n) - We traverse the list of numbers once to create the set, and in the worst case, we might traverse a sequence of numbers once.    
Space Complexity: O(n) - We store all unique numbers in the set.      

"""
def longest_consecutive(nums):
    num_set=set(nums)
    longest_streak=0
    for num in num_set:
       if num-1 not in num_set:
           current_num=num
           current_streak=1
           while current_num+1 in num_set:
               current_num+=1
               current_streak+=1
               
           longest_streak=max(longest_streak,current_streak)
    return longest_streak

if __name__=="__main__":
    nums=[100,4,200,1,3,2]
    print(longest_consecutive(nums))