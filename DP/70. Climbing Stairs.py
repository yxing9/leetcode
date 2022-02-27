# 70. Climbing Stairs
# Easy
# DP, Recursion
# 20210513


# Tabulation bottom up 10/14/2021
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [None] * n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
# Runtime: 28 ms, faster than 85.12%



# Memorization
class Solution:
    memo = {}

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        if n in self.memo:
            return self.memo[n]

        ans = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memo[n] = ans

        return ans
# 76.58%
'''
# Top down: memo with recursion -> TLE
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

'''

s = Solution()
print(s.climbStairs(3))
print(s.climbStairs(4))
print(s.climbStairs(5))