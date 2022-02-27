# 485. Max Consecutive Ones
# Easy
# https://leetcode.com/problems/max-consecutive-ones/

# Given a binary array nums, return the maximum number of consecutive 1's in the array.
'''
Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''










# 04152021
# Thoughts
# This is the first problem in Leetcode's Array Introduction chapter.
# It looks like a problem too easy. But watch for edge cases when nums start with zeros or all zeros.

# brute force 
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        temp = [] # a temporary list to store different lengths of consecutive ones
        res = [] # a result list to output the longest length among them

        for i in nums: # iterate through the list
            if i == 1: # if you find a 1, 
                temp.append(i) # add to the temporary list and
                res.append(len(temp)) # add the length of the temporary list to the reslt list
            
            else: # if it is a 0
                temp.clear() # reset by removing everything from the temporary list
                res.append(0) # you need to add a 0 to the result list in case 0 is the first or only element in nums

        return max(res)

sol = Solution()
print(sol.findMaxConsecutiveOnes([0]))
print(sol.findMaxConsecutiveOnes([0,0]))
print(sol.findMaxConsecutiveOnes([1]))
print(sol.findMaxConsecutiveOnes([1,1]))
print(sol.findMaxConsecutiveOnes([0,1,0,1,1,0]))
print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(sol.findMaxConsecutiveOnes([1,0,1,1,0,1]))
# I wrote this after three wrong submissions. 

# People on leetcode use ct = 0 to do the counting instead of an empty list that I used.
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        ct = 0
        max_ct = 0

        for i in nums:
            if i == 1:
                ct += 1

            elif i == 0:
                ct = 0

            if ct > max_ct: # NB this if cannot be written as elif or the if condition will not trigger
                max_ct = ct

        return max_ct
# These two solutions have no runtime or memory difference.

# One improvement based on the ct = 0 solution
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        ct = 0 
        max_ct = 0

        for i in nums:
            if i == 1:
                ct += 1
                if ct > max_ct:
                    max_ct = ct
            
            else:
                ct = 0

        return max_ct
# This beats 91.44%

# This is also a good solution that resonates with some of my ideas
# https://leetcode.com/problems/max-consecutive-ones/discuss/1160160/Inefficient-yet-somehow-90-time-Python-solution-with-comments