# 1295. Find Numbers with Even Number of Digits
# Easy

'''
Given an array nums of integers, return how many of them contain an even number of digits.
 

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
 

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 10^5
'''

'''
Hint #1
How to compute the number of digits of a number?

Hint #2
Divide the number by 10 again and again to get the number of digits.
'''

# Thoughts
# This is the second problem in Leetcode's Array Introduction chapter.
# Note that an integer in nums can be as large as 100,000, time complexity is important
# Response to Hint 1:
#   Method 1:
#   Treat a number as a string and return its len()
# Response to Hint 2: 
#   I don't quite understand. 

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_num = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                even_num += 1

            else:
                continue

        return even_num
# 99.41 %

sol = Solution()
print(sol.findNumbers([12,345,2,6,7896]))
print(sol.findNumbers([555,901,482,1771]))


# After Code Thoughts
# This problem is rather easy and I got it first try without revision and without error.
# And my solution is surprisingly fast. 
# After seeing others' solutions, we all using the same thing. 