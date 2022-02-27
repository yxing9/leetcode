# 905. Sort Array By Parity
# Easy
# https://leetcode.com/problems/sort-array-by-parity/


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
# time: O(n)
# space: O(1) in additional space complexity
'''

Several ways to write even and odd numbers:

even number: number % 2 == 0
odd number: number % 2 != 0 || number % 2 == 1


Another way to 
if A[i] % 2 > A[j] % 2:

'''