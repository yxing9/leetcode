# 560. Subarray Sum Equals K
# Medium




# Larry
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        larry, https://www.youtube.com/watch?v=sUoYAVuSQ2A&t=16s
        """
        # a0 + 
        
        
        prefix_seen = collections.Counter()
        current = 0
        
        prefix_seen[current] += 1
        total = 0
        
        for x in nums:
            current += x
            prev = current - k
            
            if prev in prefix_seen:
                total += prefix_seen[prev]
                
            prefix_seen[current] += 1
        
        return total
# 02/10/2022 13:46



# ====================================================================================
# Below on 04/17/2021
'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''

# I find it hard to ...
# 1. define a continuous subarrays?
# 2. how to continue with the next number if the previous one fails to add to match? Use queue

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        queue = []
        ct = 0

        for i in range(len(nums)-1):
            queue.append(nums[i])
            
            if sum(queue) == k:
                ct += 1
                queue.pop(0)

            else:
                continue

        return ct

s = Solution()
print(s.subarraySum([1,2,3],3)) # -> 1
# This solution can only count if there is a match,
# and it stops at 1 count.
# How to let it continue counting until the end of the array?
# Do I have to use recursion? 
# Can I brute force without recursion?

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pass