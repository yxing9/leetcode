# 34. Find First and Last Position of Element in Sorted numsay
# Medium
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

'''
2nd question in Binary Search Workshop assignment.
[5,7,7,8,8,10] 8
 l   m     r
       l m r
       r
'''

class Solution:
    def searchRange(self, nums, target: int):
        first = self.get_first(nums, target)
        last = self.get_last(nums, target)
        return [first, last]

    def get_first(self, nums, target):
        l, r = 0, len(nums) - 1
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                res = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return res

    def get_last(self, nums, target):
        l, r = 0, len(nums) - 1
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                res = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return res
# 87.74%, 68.43%
'''
This solution is from Leetcode Discuss.

First we find the first position:
[5,7,7,8,8,10] 8
 l   m     r
       l m r
       r

Then we find the last position:
[5,7,7,8,8,10] 8
 l   m     r
       l m r
           l
'''

# Pathrise solution
class Solution2:
    def searchRange(self, nums, target: int):
        if not nums:
            return [-1 , -1]
        return [self.findFirst(nums , target) , self.findLast(nums , target)]

    def findFirst(self, nums , target):
        l , r = 0 , len(nums) - 1
        while l + 1 < r:
            middle = (l + r) // 2
            if nums[middle] < target:
                l = middle
            else:
                r = middle
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            return -1

    def findLast(self, nums , target):
        l , r = 0 , len(nums) - 1
        while l + 1 < r:
            middle = (l + r) // 2
            if nums[middle] <= target:
                l = middle
            else:
                r = middle
        if nums[r] == target:
            return r
        elif nums[l] == target:
            return l
        else:
            return -1
# 11.33%

s = Solution2()
print(s.searchRange([5,7,7,8,8,10], 8)) # expect [3,4]
print(s.searchRange([5,7,7,8,8,10], 6)) # expect [-1,-1]
print(s.searchRange([], 0)) # expect [-1,-1]
print(s.searchRange([2,2], 2)) # expect [0,1]
print(s.searchRange([2,2,2], 2)) # expect [0,2]
print(s.searchRange([1,2,2], 2)) # expect [1,2]

'''
I tried to write a combined solution.

class Solution:
    def searchRange(self, nums, target: int):
        l, r = 0, len(nums) - 1
        res = [-1, -1]

        if len(nums) == 0:
            return res

        if nums[l] == target and nums[r] == target:
            return [l,r]

        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                r = mid
            elif nums[mid] < target:
                l = mid
            else:
                r = mid
        if nums[l] == target:
            res[0] = l
        if nums[r] == target:
            res[0] = r

        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                l = mid
            elif nums[mid] < target:
                l = mid
            else:
                r = mid
        if nums[r] == target and nums[l] != target:
            res[1] = r
        if nums[l] == target:
            res[1] = l

        return res
'''