# 198. House Robber
# Medium
# https://leetcode.com/problems/house-robber/


# I think the question can also be called:
# Largest Sum with no Adjacent Value
# or
# Larget Sum with Intervals



# 12/01/2021 update
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        
        return dp[-1]
# fallible points
# 1. don't initiate an empty list for dp like [], use [0] instead
# 2. starts with the 3rd element, so nums.length <= 2 directly return max
# 3. consequently, range starts at 2




# 08/23/2021
# DP Tabulation
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        if len(nums) <= 2:
            return max(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return dp[-1]
# refactor
class Solution:
    def rob(self, nums: List[int]) -> int:
        # or set a variable for len(nums)
        # n = len(nums)

        if len(nums) <= 2:
            return max(nums)
        # or
        # if len(nums) == 1:
        #     return nums[0]

        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        # NB dp[1] must be the greater of the two

        for i in range(2, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return dp[-1]





# Brute Force, Recursion -> TLE -> 07/26/2021
class Solution:
    def rob(self, nums):
        def rob_rec(nums, i):
            if i < 0: return 0
            current_house = nums[i] + rob_rec(nums, i-2)
            adjacant_house = rob_rec(nums, i-1)
            return max(current_house, adjacant_house)
        return rob_rec(nums, len(nums)-1)
# [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
# time: O(2^n)
# space: O(n)
# n is len(nums)



# DP Memorization Top Down -> 07262021
class Solution:
    def rob(self, nums):
        memo = [float('-inf')] * len(nums)
        
        def rob_rec(nums, i, memo):
            if i < 0: 
                return 0
            
            if memo[i] != float('-inf'):
                return memo[i]

            current_house = nums[i] + rob_rec(nums, i-2, memo)
            adjacant_house = rob_rec(nums, i-1, memo)
            
            memo[i] = max(current_house, adjacant_house)
            
            return memo[i]
        
        return rob_rec(nums, len(nums)-1, memo)
# time: O(n)
# space: O(n)
# v2: DP Memo Top Down using a hashmap -> 07272021
class Solution:
    def rob(self, nums):
        memo = {}
        def rob_rec(nums, i, memo):
            if i < 0: 
                return 0
            if i in memo:
                return memo[i]
            current_house = nums[i] + rob_rec(nums, i-2, memo)
            adjacant_house = rob_rec(nums, i-1, memo)
            memo[i] = max(current_house, adjacant_house)
            return memo[i]
        return rob_rec(nums, len(nums)-1, memo)




# Solution 1: DP Table, 05072021 -> Tablulation Bottom Up
'''

1,2,3,1
1   4
      2
  2   3
    3

A lot more to learn in the Discuss session.
https://leetcode.com/problems/house-robber/discuss/?currentPage=1&orderBy=most_votes&query=

'''
class Solution:
    def rob(self, nums) -> int:
        amount = [0] * (len(nums) + 1)
        amount[1] = nums[0]
        i = 2

        for num in nums[1:]:
            amount[i] = max(num + amount[i-2], amount[i-1])
            i += 1

        return amount[-1]
# 82.84%
'''
1. Why the length of "amount" is "len(nums) + 1"?
2. Why the first element in "amount" is 0?
3. Why is "i" initially set to 2?
4. Why "nums[1:]"?
5. Why "return amount[-1]"?

Here is the logic that answers all questions:

[2, 7, 9, 3, 1]     * If we want to choose 7 as the starting point instead of 2, 
[0, 2               * imagine there is a 0 before the list.

      7+0,2         * This is how we achieve intermittent addition.
[0, 2,  7

         9+2,7
[0, 2, 7,  11

             3+7,11
[0, 2, 7, 11,  11

                 1+11, 11
[0, 2, 7, 11, 11,   12


Let's take [2,7,9,6,3] as another example.

         max(9+2,7+0)
[0, 2, 7,    11

             max(6+7,9+2)
[0, 2, 7, 11,    13

                 max(3+9+2,6+7)
[0, 2, 7, 11, 13,     14]

I still need to know how people come up with this genius solution.
'''

# Test Cases
s = Solution()
print(s.rob([1])) # -> 1
print(s.rob([1,2,3,1])) # -> 4
print(s.rob([2,7,9,3,1])) # -> 12
print(s.rob([2,12,9,3,1])) # -> 15
print(s.rob([2,7,9,6,3])) # -> 14