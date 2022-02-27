# 746. Min Cost Climbing Stairs
# Easy
# https://leetcode.com/problems/min-cost-climbing-stairs/


# DP Tabulation, backward
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[n-1] = cost[n-1]
        dp[n-2] = cost[n-2]
        for i in range(n-3, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        return min(dp[0], dp[1])
# time: O()
# space: O()


# DP Tabulation, forward
# Yu Zhou on leetcode discuss
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n

        # base
        dp[0] = cost[0]
        dp[1] = cost[1]

        # recurrence
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1], dp[-2])
'''

Forward is more intuitive for me.

'''