# 162. Find Peak Element
# Medium
# https://leetcode.com/problems/find-peak-element/

'''
4th question in Binary Search Workshop assignment.
852. Peak Index in a Mountain Array is the easier version.

Questions:
1. Will there be at least one peak? Yes
2. 

[1,2,3,1] 2
 0 1 2 3
 l m   r

[1,2,1,3,5,6,4] 1 or 5
 0 1 2 3 4 5 6
 l     m     r


if arr[mid] > arr[mid + 1]:
    r moves towards center
if arr[mid] < arr[mid + 1]:
    l moves to right
'''

class Solution:
    def findPeakElement(self, nums) -> int:
        l, r = 0, len(nums) - 1
        while l < r: # TLE: l <= r
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid # Wrong Answer: r = mid + 1
            else:
                l = mid + 1
        return l
# Time: O(logn)
'''
This is leetcode solution.

My questions:
1. Why l <= r won't work?
2. why r = mid but l = mid + 1?
'''

# Pathrise solution
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l , mid , r = 0, 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r-l)//2
            if nums[mid] < nums[mid + 1]:
                l = mid
            else:
                r = mid 
        if nums[l] > nums[r]: return l
        else: return r
# 91.19%

s = Solution()
print(s.findPeakElement([1,2,3,1])) # expect 2
print(s.findPeakElement([1,2,1,3,5,6,4])) # expect 5