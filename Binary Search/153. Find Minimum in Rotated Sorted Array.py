# 153. Find Minimum in Rotated Sorted Array
# Medium
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

'''
5th question in Binary Search Workshop assignment.

N.B. carefully walk through all edge cases
1. return the element of the array, NOT its index
2. arr.length starts from 1
3. distinct/unique element


[3,4,5,1,2]
 0 1 2 3 4
 l   m   r
     l


! An important take-away from this question:
Two minor tweaks may both work for a test case, 
but we need to find that final version of codes 
that works for all edge cases (universally).
It's like finetuning a machine, from general 
to specific.

1. Why "while l < r" not "while l <= r"?
Because of edge case when arr.length == 1 and 
the existence of [mid + 1], we can't let "l <= r".

2. Why "l = mid + 1" not "l = mid"?
Based on "l < r", if I let "l = mid", l will stuck at 5 or 7, 
while r makes its way towards l and exits the while loop.

When nums[mid] is greater than the next element, 
mid is definitely not the answer we are looking for.
So we just skip mid and let l equal to mid's next one.

3. Why "r = mid" not "r = mid - 1"?
Similar to 2 above. When arr[mid] is smaller than the next element, 
we can't rule out the possiblity than mid is not the smallest element.
Therefore we can't let r skip mid and move to mid - 1.

ALL TEST CASES THIS CODE PASSED ARE ACTUALLY EDGE CASES WHERE 
arr[mid + 1] IS THE INFLECTION POINT.

!! A more important take-away from this question:
Finetuning your code based on a wrong framework leads to nowhere.
You need to find a more general pattern/framework.
Finding a pattern.


class SolutionFailed:
    def findMin(self, nums) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

if nums[mid] > nums[mid + 1]:
    return nums[mid + 1]
'''

class Solution:
    def findMin(self, nums) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] >= nums[l] and nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[l]
# Time O(logn)
# 64.45%
'''
Solution from Nick White.
Note that "nums[mid] >= nums[l]" can't be "nums[mid] > nums[l]", 
or this edge case [2,3,4,5,1] is wrong.
'''

class Solution2:
    def findMin(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        if nums[0] < nums[r]:
            return nums[0]

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1
# 96.87%, 64.45%
'''
Leetcode solution
'''

# pathrise solution
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , mid , r = 0, 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid
            else:
                r = mid
        return min(nums[l], nums[r])
# 27.11%

s = Solution2()
print(s.findMin([1])) # expect 1
print(s.findMin([3,4,5,1,2])) # expect 1
print(s.findMin([4,5,6,7,0,1,2])) # expect 0
print(s.findMin([11,13,15,17])) # expect 11
print(s.findMin([3,1,2])) # expect 1
print(s.findMin([2,3,4,5,1])) # expect 1
print(s.findMin([3,4,5,6,1,2])) # expect 1