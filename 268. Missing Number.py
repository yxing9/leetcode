# 268. Missing Number
# E


# Larry, https://www.youtube.com/watch?v=ob1fUZCyr1E
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # x * (x + 1) / 2
        N = len(nums) + 1 - 1
        
        totalf = N * (N + 1) // 2
        totals = sum(nums)
        
        return totalf - totals
# 05/30/2022 15:25



# My solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        n == nums.length
        """
        n = len(nums)
        ref = [_ for _ in range(n + 1)]
        ans = 0
        
        for _ in ref:
            if _ not in nums:
                ans = _
            else:
                continue
                
        return ans
# 05/28/2022 14:26
# O(n) time, n is nums.length
# O(n) space, for the extra reference array