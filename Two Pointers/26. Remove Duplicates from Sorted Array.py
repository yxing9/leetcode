# 26. Remove Duplicates from Sorted Array
# Easy

# Solution 1: Two Pointers
class Solution1:
    def removeDuplicates(self, nums) -> int:

        l, r = 0, 1

        while r <= len(nums) - 1:
            if nums[l] == nums[r]:
                r += 1
            else:
                nums[l+1] = nums[r]
                l += 1

        return nums[:l + 1] # l + 1
# 79.45%
'''
This solution is faily easy to think of. 
But I spent quite some time on some minor details.
e.g.
1. Why it has to be l+=1 but not l=r as I tried before?
    - l should be checked and updated one by one

        0,0,1,1,1,2,2,3,3,4
        l r
        l   r
        0,1,1,1,1,2,2,3,3,4
          l r
           l   r

2. Why the two conditions, if len(nums)==0 or 1, are not needed?
    - if len(nums)==0, then while r<=-1 is invalid as r==1, then l+1 as 1 is returned, which is []
    - if len(nums)==1, then while r<=0 is invalid as r==1, then l+1 as 1 is returned, which is nums itself


Solution 1 is an improved version based on the following solution.

class Solution:
    def removeDuplicates(self, nums) -> int:

        0,0,1,1,1,2,2,3,3,4
        l r
        l   r
            l     r
                      l   r

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        l = 0
        r = 1

        while r <= len(nums) - 1:
            if nums[l] == nums[r]:
                r += 1
            else:
                nums[l+1] = nums[r]
                l += 1

        return nums # l + 1
# 45.55% 
'''

# Solution 2:

#for i in range(len(nums)):


# Testcase
s = Solution1()
print(s.removeDuplicates([1,1,2])) #-> 2, nums = [1,2]
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) #-> 5, nums = [0,1,2,3,4]
print(s.removeDuplicates(([])))
print(s.removeDuplicates(([1])))
print(s.removeDuplicates(([3,3]))) 