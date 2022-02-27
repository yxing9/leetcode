# 121. Best Time to Buy and Sell Stock
# Easy
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# dp series:
# 152. Maximum Product Subarray -> 53. Maximum Subarray -> 121.



# ============================================================================================

# 01/31/2022
# 1st try after 2 months
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        
        if N <= 1:
            return 0
        
        dp = [0] * N
        
        for i in range(1, N):
            dp[i] = max(dp[i-1], prices[i] - prices[i-1])
            
        return dp[-1]
# I forgot dp[0][0] = [prices[0], 0] # set dp[..][..] to min(price) and max(profit)

# 2nd try after peeking
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        
        dp = [[0, 0]] * N
        dp[0][0] = prices[0]
        dp[0][1] = 0
        
        for i in range(1, N):
            dp[i][0] = min(dp[i-1][0], prices[i])
            dp[i][1] = max(dp[i][1], prices[i] - dp[i][0]) # NB, i not i-1
            
        return dp[-1][1]
# 01/31/2022 23:32

# 3rd fix
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        
        dp = [[0, 0]] * N
        dp[0][0] = prices[0]
        dp[0][1] = 0
        
        for i in range(1, N):
            dp[i][0] = min(dp[i][0], prices[i]) # NB, i not i-1
            dp[i][1] = max(dp[i][1], prices[i] - dp[i][0])
            
        return dp[-1][1]
# 01/31/2022 23:35
"""
dp[i][0] = min(dp[i][0], prices[i])
dp[i][1] = max(dp[i][1], prices[i] - dp[i][0])

dp[i][0] = min(dp[i-1][0], prices[i])
dp[i][1] = max(dp[i-1][1], prices[i] - dp[i-1][0])

Both of them work.
Why?
Because it doesn't matter if you compare current or previous dp[i][0] or dp[i][1] 
to prices[i] - ..., we are getting the result from prices anyway.


"""




# ============================================================================================

# dp
# 12/05/2021
# [prices[0],0] inspired by https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/1545423/Python-easy-to-understand-solution-with-explanation-%3A-Tracking-and-Dynamic-programming
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0,0]] * n
        dp[0] = [prices[0], 0] # set min price and max profit
        for i in range(1, n):
            dp[i][0] = min(dp[i-1][0], prices[i]) # min price: either update or stay put
            dp[i][1] = max(dp[i-1][1], prices[i]-dp[i-1][0]) # max profit: either update or stay put
        return dp[-1][1]
# Runtime: 1312 ms, faster than 20.25%
# time O(n)
# space O(n)



# Two Pointers
'''
[7,1,5,3,6,4]
 l         r
 

'''

# ----

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        sliding window from neetcode
        '''
        l, r = 0, 1
        max_profit = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1

        return max_profit
# time: O(n)
# space: O(1)


# ----


# from lc discuss
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit
# Runtime: 1076 ms, faster than 68.60%
# time: O(n)
# space: O(1)


# ----


# my failed solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        temp = 0
        # mx = 0
        # mn = 0
        for i in range(1, n):
            for j in range(i):
                if prices[i] - prices[j] > temp:
                    temp = prices[i] - prices[j]
                dp[i] = max(dp[i-1], temp)
        return dp[-1]
# 198 / 211 test cases passed.


# ----


# BF - TLE (Time Limit Exceeded)
class Solution:
    def maxProfit(self, prices) -> int:
        maxPrice = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > maxPrice:
                    maxPrice = prices[j] - prices[i]
        return maxPrice
# runtime O(n^2)
# TLE but we can take O(n^2) runtime as the baseline.

'''
This was code I wrote
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        def backtracking(i, prices):
            if i+1 == len(prices):
                return
            for day in range(i, len(prices)-1):
                if prices[day+1] - prices[day] > maxPrice:
                    maxPrice = prices[day+1] - prices[day]
            backtracking(i+1, prices, maxPrice)
        backtracking(0, prices)
        return maxPrice
'''

s = Solution()
print(s.maxProfit([7,1,5,3,6,4])) # expect 5
print(s.maxProfit([7,6,4,3,1])) # expect 0



# --- END --- #