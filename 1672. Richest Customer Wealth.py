# 1672. Richest Customer Wealth
# Easy


# my 1st
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        ans = sum(accounts[0])
        for i in accounts:
            if ans < sum(i):
                ans = sum(i)
        return ans
# 01/30/2022 19:17
# time O(M * N), M == accounts.length, N == accounts[i].length
# space O(1)


# my 2nd, lc solution, approach 1
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for i in accounts:
            ans = max(sum(i), ans)
        return ans
# 01/30/2022 21:10
# changed if statement to max()


# Larry's, https://www.youtube.com/watch?v=-cHIIXgxFSg
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(customer_account) for customer_account in accounts)
# 01/30/2022 23:28



# --- END --- #