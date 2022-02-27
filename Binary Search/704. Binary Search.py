# 704. Binary Search
# Easy

# Thoughts Before Coding
'''
This is the first and introductory question in Leetcode's Binary Search chapter.

Note that the array is sorted in ascending order.
All integers in the array are unique.

"len(nums)" can be odd or even
    - if it's odd, "mid" is the favorably the middle number that splits the array evenly
        - "mid = (l + r) // 2"
    - if it's even:
        - "mid = (l + r) // 2" is the middle left number
        - "mid = (l + r) // 2 + 1" is the middle right number
* But this turns out to be irrelevant. 
'''

# Solution: Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            pivot = left + (right - left) // 2 # "pivot = (left + right) // 2" is what I wrote, but unfortunately it is a bug

            if target < nums[pivot]:
                right = pivot - 1

            elif target > nums[pivot]:
                left = pivot + 1

            else:
                return pivot

        return -1
# 59.62%, 96.75%, 78.29%, 78.29%, 78.29%, 39.18%
# Time O(log(n)), Space O(1)
# pivot = left + (right - left) // 2 and other lines unchanged
# 91.00%, 12.91%, 99.09%, 91.00%, 78.29%, 39.18%, 91.00%, 78.29%, 78.29%
# Seems like they have similar runtime but the second one is seemingly faster.
# But when it comes to numbers, runtime ranges from 220 ms to 248 ms, not a big difference?
'''
I wrote this code after turning to Leetcode Solution for help.
It is written in my style and easier for me to understand than the Leetcode Solution.

Some points to be noticed:
1. "pivot = left + (right - left) // 2"
    - "pivot = (left + right) // 2" is actually a bug 
    - according to https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html.
    - Runtime jumps to 228 ms with 91.00% when it is "pivot = left + (right - left) // 2" with "right = pivot - 1" and "left = pivot + 1".

2. "right = pivot - 1" and "left = pivot + 1"
    - When I changed them to "right = pivot" and "left = pivot", I got "Time Limit Exceeded" error.
        - Because if there is only one element in the list and "l" is set to equal "m" (l = m), 
          we will get an infinite loop.

Where did I get this wrong:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        mid = (l + r) // 2
        index = -1

        for i in range(len(nums)):
            if target < nums[mid]:
                r = mid
            elif target > nums[mid]:
                l = mid
            elif target == nums[mid]:
                index = mid

        return index

1. I thought "index" is optional or doesn't hurt to have it there. 
    - But it actually caused runtime error.

2. As "mid" is a changing variable, it have to be placed inside the loop.

3. As we need to update "left" and "right", we have to use a while loop but not a for loop.
    - Because "for" has a direct relationship with indexes of "nums"
    - but what we actually care about is updating "mid"
    - which is not affected by iterating through "nums".
'''