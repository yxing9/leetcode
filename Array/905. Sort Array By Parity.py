# 905. Sort Array By Parity
# Easy


# Larry, youtube.com/watch?v=d_IP1cWghZM
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        """
           v
        [0,1,0,1,1,0,1,1,0,1,1]
           ^             ^
        """
        
        left = 0
        right = N - 1
        
        while left < right:
            while left < N and nums[left] % 2 == 0:
                left += 1
                
            while right >= 0 and nums[right] % 2 == 1:
                right -= 1
                
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                
        return nums
# 05/03/2022 21:45
# O(N) time
# O(1) space
# in-place
"""
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        def f(x):
            if (x % 2 == 0):
                return -x
            else:
                return x

        A.sort(key=lambda x: f(x))
        return A
"""

# Larry, https://www.youtube.com/watch?v=d_IP1cWghZM
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x % 2)
# 05/03/2022 21:11


# my solution using deque
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = collections.deque()
        
        for _ in nums:
            if _ % 2 == 0:
                ans.appendleft(_)
            else:
                ans.append(_)
                
        return ans
# 05/02/2022 17:20

# ----------
# 8.1.2021
# Two Pointers
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l] % 2 != 0 and nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            elif nums[l] % 2 == 0:
                l += 1
            elif nums[r] % 2 != 0:
                r -= 1
        return nums
# 08/01/2021 20:33
# time: O(n)
# space: O(1) in additional space complexity
'''

Several ways to write even and odd numbers:

even number: number % 2 == 0
odd number: number % 2 != 0 || number % 2 == 1


Another way to 
if A[i] % 2 > A[j] % 2:

'''