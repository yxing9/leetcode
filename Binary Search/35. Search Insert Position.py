# 35. Search Insert Position
# Easy
# https://leetcode.com/problems/search-insert-position/

'''
1st question in the assignment 
after SWE Workshop 3 Binary Search.

Follow the basic post processing template:

def find_nearest(arr, target):
    l, r = 0, len(arr) - 1
    while l + 1 < r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            l = mid
        else:
            r = mid

    # post processing
    if abs(target - arr[l]) <= abs(target - arr[r]):
        return l
    else:
        return r

But add a comparison part to check before and after.
'''

class Solution:
    def searchInsert(self, nums, target: int) -> int:
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid
            else:
                r = mid

        if abs(target - nums[l]) <= abs(target - nums[r]):
            if target > nums[l]:
                return l + 1
            else:
                return l
        else:
            if target > nums[r]:
                return r + 1
            else:
                return r
# 37.39%

# Pathrise solution
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0: return 0
        l , r = 0 , len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] == target: 
                return mid
            elif nums[mid] < target:
                l = mid
            else:
                r = mid
        # Post
        if nums[l] == target: return l     # [1] | 1
        if nums[r] == target: return r     # [1, 2] | 2
        if nums[l] > target: return l      # [1, 3, 5, 6] | 0
        if nums[l] < target < nums[r]:     # [1,2,4,5] | 3
            return l + 1
        if nums[r] < target:               # [3, 5] | 9
            return r + 1
# 37.54%

s = Solution()
print(s.searchInsert([1,3,5,6], 5)) # expect 2
print(s.searchInsert([1,3,5,6], 2)) # expect 1
print(s.searchInsert([1,3,5,6], 7)) # expect 4
print(s.searchInsert([1,3,5,6], 0)) # expect 0
print(s.searchInsert([1], 0)) # expect 0