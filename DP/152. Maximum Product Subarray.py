# 152. Maximum Product Subarray
# Medium
# dp
# 53

'''

I have to know why this can't be a sliding window question.
Because:
Sometimes when you move the left boundary of the window when the current product is negative, 
it might be a mistake because the next number might be a negative thus the product becomes positive 
that might be higher than what you previously have.



        I initially don't understand why this is a dp problem.
        
        after drawing a desicion tree, I start to see
        
        
        [2,3,-2,-4]
        
                 2          3        -2       -4
                / \        / \       / \ 
               3   x     -2   x    -4   x
              / \        / \ 
            -2   x     -4   x
            / \        
          -4   x
        
          48  -12 6 2  24   -6 3    8   -2    -4


The difference b/t 152 and 53 is that 
in 152 because of multiplication, 
a negative number that appeared before might become positive and bigger.


'''


# dp 12/06/2021
# refactor based on the failed dp solution below
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_dp = [nums[0]] * n
        min_dp = [nums[0]] * n
        for i in range(1, n):
            max_dp[i] = max(nums[i]*max_dp[i-1], nums[i]*min_dp[i-1], nums[i])
            min_dp[i] = min(nums[i]*max_dp[i-1], nums[i]*min_dp[i-1], nums[i])
        return max(max_dp) # max_dp[-1] is incorrect
# Runtime: 56 ms, faster than 62.10%
# time O(n)
# space O(n)

# refactor to O(1) space
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_product = nums[0]
        min_product = nums[0]
        ans = nums[0]
        for i in range(1, n):
            temp = max_product
            max_product = max(nums[i]*max_product, nums[i]*min_product, nums[i])
            min_product = min(nums[i]*temp, nums[i]*min_product, nums[i])
            ans = max(max_product, ans)
        return ans
# Runtime: 48 ms, faster than 94.23%
# time O(n)
# space O(1)



# ----------------------

# dp failed solution
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
                            Output      Expected
        [2,3,-2,4]          6           6
        [2,-3,-2,4]         48          48
        [0]                 0           0
        [0,2]               2           2
        [-2]                -2          -2
        [2,-5,-2,-4,3]      480         24          failed

        '''
        n = len(nums)
        dp = [[nums[0], nums[0]]] * n
        ans = nums[0]
        for i in range(1, n):
            dp[i][0] = max(nums[i], nums[i]*dp[i-1][0], nums[i]*dp[i-1][1])
            dp[i][1] = min(nums[i], nums[i]*dp[i-1][0], nums[i]*dp[i-1][1])
            ans = max(ans, dp[i][0])
        return ans
# I don't know why this failed


# -----------------------------

# 1st wrong solution 12/03/2021
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        
        sliding window?
        
        '''
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        l, r = 0, 1
        ans = nums[l] * nums[r]
        
        while r < n:
            ans = max(ans, nums[l] * nums[r])
            l += 1
            r += 1
        
        return ans
# 2nd wrong solution
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        
        sliding window?
        
        the edge case of [0,2] expect 2 means the subarray can be a length of 1
        this is not sliding window then
        this makes the question more difficult
        
        '''
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        l, r = 0, 1
        ans = nums[l] * nums[r]
        
        while r < n:
            ans = max(ans, nums[l] * nums[r])
            l += 1
            r += 1
        
        if ans < max(nums):
            return max(nums)
        return ans
# 3rd wrong solution
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        
        sliding window?
        
        the edge case of [0,2] expect 2 
        means the subarray can be a length of 1
        this is not sliding window then
        this makes the question slightly more difficult, add two lines of code
        
        the edge case of [-2,3,-4] expect 24 
        means the subarray can be any length
        this is again sliding window
        '''
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        l, r = 0, 1
        ans = 1
        temp = 1
        
        while r < n and l <= r:
            for i in range(l, r+1):
                temp *= nums[i]
            if temp > ans:
                ans = temp
                r += 1
            l += 1
            
        return ans
# [2,3,-2,4]
# [0,2]
# [-2,3,-4]
# output
# 288
# 1
# 1
# expect
# 6
# 2
# 24