# 53. Maximum Subarray
# Easy
# 121, 53, 152

'''

Doesn't feel like an easy question

Why can't use sliding window? 
same reason as 152?


Even the brute force solution doesn't feel like easy.



Why I don't know how to write a dp solution?
Because I don't how to compare or choose among multiple choices, 
e.g. max(-2+1-3+4, 1-3+4, -3+4, 4), this keeps growing


Breaking a dp problem down to subproblems:
If it were ending here ... 

index  0   1     2    3     4    5       6        7           8
     [-2,  1,   -3,   4,   -1,   2,      1,      -5,          4]
dp = [-2,  1,   -2,   4,    3,   5,      6,      -1,          5]
      -2
           1
                1-3
                      4
                           4-1
                                 (4-1)+2
                                       (4-1+2)+1
                                                (4-1+2+1)-5
                                                           (4-1+2+1-5)+4
then the two choices are:
continue
or 
start new from here
=> dp[i] = max(dp[i-1]+nums[i], nums[i])



Conclusion:

1. Just like playing a detective's game, drawing every evidence helps seeing the pattern a lot more clear.

2. Evidence to use dp: arriving at global optimum from local optima.

'''



# dp
# 12/06/2021
# finally i got the dp solution by myself with the help of https://www.youtube.com/watch?v=2MmGzdiKR9Y&t=1s
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = ['-inf'] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)
# Runtime: 724 ms, faster than 78.44%
# time O(n)
# space O(n)
# The essence is choose b/t continue or start new from here.

# refactor to O(1) space
# this is also dp just leaves out the list, use max_subarray to keep track of the max sum
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = nums[0]
        max_subarray = nums[0]
        for i in range(1, len(nums)):
            current_subarray = max(current_subarray+nums[i], nums[i])
            max_subarray = max(current_subarray, max_subarray)
        return max_subarray
# Runtime: 788 ms, faster than 40.22%
# time O(n)
# space O(1)


# --

# Kadane's 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = max_global = nums[0]
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            if max_current > max_global:
                max_global = max_current
        return max_global
# Runtime: 724 ms, faster than 78.44%
# time O(n)
# space O(1)
# Turns out to be the same as dp


#----------------------------------------

# Optimized Brute Force LeetCode solution
import math
class Solution:
    '''

    The trick is to recognize that all of the subarrays starting at a particular value will share a common prefix.

    originally O(n^3):

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            current_subarray = 0
            for k in range(i, j+1): # we need this because we need to add every number between i and j and store the max
                current_subarray += nums[k]
            max_subarray = max(max_subarray, current_subarray)
    return max_subarray

    '''
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)
        return max_subarray
# TLE
# time O(n^2)
# space O(1)
# Even this is hard to understand