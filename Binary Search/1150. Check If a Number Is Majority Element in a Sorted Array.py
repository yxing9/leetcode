# 1150. Check If a Number Is Majority Element in a Sorted Array
# Easy
# Binary Search
# mocking interview with daniel kim on 11/24/2021
# Similar questions:
# 169. Majority Element
# 229. Majority Element II



# +----------------------------------------+-----------------+------------------+-
# | Algorithms and/or Data Structures Used | Time Complexity | Space Complexity |
# +----------------------------------------+-----------------+------------------+-
# |             binary search              |     O(log n)    |       O(1)       |
# +----------------------------------------+-----------------+------------------+-
# |                hash map                |       O(n)      |       O(n)       |
# +----------------------------------------+-----------------+------------------+-
# |               two pointers             |       O(n)      |       O(1)       |
# +----------------------------------------+-----------------+------------------+-




'''
    Check If a Number Is Majority Element in a Sorted Array

    Given an array nums sorted in non-decreasing order and a number target, 
    return true if and only if target is a majority element.
    A majority element is an element that appears more than N/2 times in an array of length N.

    Example 1:
    Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
    Output: true

    Example 2:
    Input: nums = [10,100,101,101], target = 101
    Output: false

    public boolean isMajorityElement(int[] nums, int target) {
        
    }
'''



# binary search
# 11/25/2021
# template for finding the left boundary
# my solution with hint on the next day's morning
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        '''
        find the left boundary
        '''
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r-l) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        r = l + len(nums) // 2
        return r < len(nums) and nums[r] == target
# Runtime: 50 ms, faster than 25.79%
# time: O(log n)
# space: O(1)
# i can use some refactors here to make the code communicate even better
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        def bsearch(nums, target):
            l, r = 0, len(nums)-1
            while l < r:
                m = l + (r-l) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l
        l = bsearch(nums, target)
        r = l + len(nums) // 2
        return r < len(nums) and nums[r] == target
# Runtime: 42 ms, faster than 30.98%



#-------------------------------------------
# live mock interview code
def isMajorityElement(nums, target):

    def helperLeft(nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = l + (r-l) // 2
            if nums[m] == target:
                r = m
            elif m < target:
                l = m
            if l == target:
                return l
            if r == target:
                return r
    
    def bsearch(nums, target):
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) / 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l
    # 1 2 3 4, target = 2
    # l = 1
    # r = 1 + 2 = 3, num[r] != target

    # 1 2 2 2 2 2 2 2 2 3, target = 2
    # l = 1
    # r = 1 + 5 = 6, nums[r] == target

    # 1 1 1 1 1 2 3, target = 2
    # l = 5
    # r = 5 + 3 = 8, out of bounds

    l = bsearch(nums, target)
    r = l + len(nums) / 2

    return r < len(nums) and nums[r] == target
        
    # def helperLeft(nums, target):
    #     l, r = 0, len(nums)
    #     while l < r:
    #         m = l + (r-l) // 2
    #         if m == target:
    #             l = m
    #         elif m < target:
    #             r = m
    #         if l == target:
    #             return l
    #         if r == target:
    #             return r

