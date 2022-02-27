# 162. Find Peak Element
# 2nd Try

'''

You must write an algorithm that runs in O(log n) time.
=> this is the trigger to use binary search
=> I missed it.


1 <= nums.length <= 1000

nums[i] != nums[i + 1] for all valid i. 
=> no same values next to each other


Even though it does not state clearly in the question, 
there is at lease one peak element in the array. 

Our goal is just to find that peak.


[1,2,3,1]
 l m   r


*Why you only need to compare if nums[i] > nums[i+1]?
Consider ascending, descending, and peak:
1. ascending: nums[i] > nums[i+1] never gets satisfied, indicating we are on a rising slope, 
so we return the last element as the peak.

2. descending: only the first element satisfies nums[i] > nums[i+1],
return the first element, which is i, directly.

3. peak: 
When we are on the rising side, nums[i] > nums[i+1] will not get satisfied until at the peak, 
return i directly.

'''


# Binary Search: Iterative
class Solution:
    def findPeakElement(self, nums) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2




# Brute Force: linear scan
# class Solution:
#     def findPeakElement(self, nums) -> int:
#         if len(nums) == 1:
#             return 0
#         for i in range(len(nums)):
#             if i == 0 and nums[i] > nums[i+1]:
#                 return i
#             if i == len(nums) - 1 and nums[i] > nums[i-1]:
#                 return i
#             if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
#                 return i
#         return None
# time: O(n)
# space: O(1)
'''

The reason why the 3rd if condition will not trigger an 'out of range' error
is that it will not go this far before all conditions has been found.

This implies in this question 
there must be at least ONE peak element in the array. 

'''
# Revise after leetcode solution:
# class Solution:
#     def findPeakElement(self, nums) -> int:
#         for i in range(len(nums)-1):
#             if nums[i] > nums[i+1]:
#                 return i
#         return len(nums)-1
# time: O(n)
# space: O(1)
s = Solution()
print(s.findPeakElement([1,2,3,1])) # expected 2
print(s.findPeakElement([1,2,1,3,5,6,4])) # expected 1 or 5
print(s.findPeakElement([2,1,0,3,5,6,7])) # expected 0 or 6
print(s.findPeakElement([1])) # expected 0
print(s.findPeakElement([2,1])) # expected 0