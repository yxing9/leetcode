# 27. Remove Element
# Easy



# Two Pointers 04/30/2021 Solution 1: 
class Solution1:
    def removeElement(self, nums, val: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] != val:
                l += 1
            elif nums[r] == val:
                r -= 1
            elif nums[l] == val and nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
        
        return l # nums[:l] is the actual output in leetcode
        # , but if I change it to return nums[:l] there will be an error
# 98.01%
# time: O(n) n is len(nums)
# space: O(1)
'''
Solution1 is improved based on below:

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        ct = 0

        while l < r:
            if nums[l] != val:
                l += 1
            elif nums[r] == val:
                r -= 1
            elif nums[l] == val and nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                ct += 1
        
        return len(nums) - ct - 1

Testcase                Output          Expected
[3,2,2,3] 3             [2,2]           [2,2]
[0,1,2,2,3,0,4,2] 2     [0,1,4,0,3]     [0,1,4,0,3]
[2] 3                   []              [2]
[1] 1                   []              []
[3,3] 3                 [3]             []

As we can see, this solution can't handle length 1 and elements = val

N.B.: while l <= r must have the equal = sign or [2] 3 outputs [] which is wrong

N.B.: There is no need to have ct as l tracks count better because 
l += 1 every time two numbers are swapped, and 
the equal sign in <= makes sure l stops at the last number that is not equal to val. 
'''


# Two Pointers 08042021
# leetcode solution 2
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            if nums[l] == val:
                nums[l] = nums[r-1]
                r -= 1
            else:
                l +=1 
        return l
'''

Advance l to the next one only when nums[l] is not the target value.

This is smarter way to implement two pointers.

'''


# another Two Pointers solution brought up by Pathrise 08042021
# Read-Write Pointers
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        wr, rd = 0, 0
        while rd < len(nums):
            if nums[rd] != val:
                nums[wr] = nums[rd]
                wr += 1
            rd += 1
        return wr
# the rd pointer takes the lead 
# only when rd pointer is not target value, wt pointers moves forward
# wr pointer follows
# this is also a smarter way



# Solution 2: 04/30/2021
# sample 16 ms submission on leetcode
class Solution2:
    def removeElement(nums, val):
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j
# 40.32%
# This is not my solution. 
# It takes 36 ms surprisingly lower than it says 16 ms.
# time: O(n) n is len(nums)
# space: O(1)




# Note:
'''

Two pointers swap an element and the target value, and put the target value 
to the end of the array.

The second solution remakes the array by copying non-target value to the 
beginning of the array.
It reflects the Hint 3.

'''

# Testcase
s = Solution1()
# s2 = Solution2()
print(s.removeElement([3,2,2,3], 3)) #-> 2, nums = [2,2]
print(s.removeElement([0,1,2,2,3,0,4,2], 2)) #-> 5, nums = [0,1,4,0,3]
print(s.removeElement([2], 3)) #-> 0, nums = [2]
print(s.removeElement([1], 1)) #-> 0, nums = []
print(s.removeElement([3,3], 3)) #-> 0, nums = []