# 75. Sort Colors
# The Dutch Flag Problem
# Medium


# Two Pointers
'''

Where this problem is hard is that 
using two-pass to first put 0's in the front
then put 2's to the back

I was trying to do this in one-pass.

'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        
        # put 0's upfront
        while l < r:
            if nums[l] != 0 and nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            elif nums[l] == 0:
                l += 1
            elif nums[r] != 0:
                r -= 1
                
        # put 2's to the back
        r = len(nums)-1
        while l < r:
            if nums[l] == 2 and nums[r] != 2:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            elif nums[l] != 2:
                l += 1
            elif nums[r] == 2:
                r -= 1
# time: O(n) n is len(nums)
# space: O(1)



# Counting Sort
# but still uses two pointers
'''

For this counting sort solution, it satifies the in-place requirement, 
but it's not using constant extra space. 
Space complexity can be O(n) at worst for creating the counting array. 

'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # first pass to create a counter
        ct = {}
        for i in range(len(nums)):
            if nums[i] not in ct:
                ct[nums[i]] = 0
            ct[nums[i]] += 1

        # second pass to reconstruct nums
        l, r = 0, len(nums)-1
        for j in ct:
            if j == 0:
                while ct[j] > 0:
                    nums[l] = j
                    ct[j] -= 1
                    l += 1
            elif j == 2:
                while ct[j] > 0:
                    nums[r] = j
                    ct[j] -= 1
                    r -= 1
        for _ in range(l, r+1):
            nums[_] = 1
# time: O(n + n) essentially O(n), same as above
# space: O() extra space for hashmap
'''

Don't have to use a hashmap to store the counter.

def sortColors(nums):
    count0, count1 = 0, 0
    for num in nums:
        if num == 0: count0 += 1
        elif num == 1: count1 += 1
    i = 0
    for i in range(count0):
        nums[i] = 0
    for i in range(count0, count0+count1):
        nums[i] = 1
    for i in range(count0+count1, len(nums)):
        nums[i] = 2

'''