# 1. Two Sum
# Easy

# Solutions
'''
1. Brute force
    - enumerate()

2. Hash table
    - 2.1. two pass
    - 2.2. one pass
    - enumerate() or range(len())

3. Two pointers

4. Binary search
    - for faster searching than for loop
'''

# 1. Brute force with enumerate()
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            for i2, n2 in enumerate(nums):
                if n + n2 == target and i != i2:
                    return [i, i2]
# 57.89%
'''
This is surprisingly faster than all other approaches and is intuitive to understand.

Variant on Solution 1:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if num + nums[j] == target:
                    return [i, j]
# 100%

This solution answers my confusion when I was stuck with those failed submissions by using enumerate() only in one for loop.
This approves my thinking was on the right track. Great learning.
'''

# 2. Hash table
# 2.1. Hash table: one pass using enumerate()
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i, num in enumerate(nums):
            if target - num in dct: # if ... in dct looks for keys in dictionary
                return [dct[target - num], i] # gets us the value in the dictionary, which is the index that we want
            else: # else is optional, doesn't affect runtime without else
                dct[num] = i # adds value,key to dictionary instead of key,value so its index (which is the key) can be returned
# 57.69%
# Time O(n)
# Space O(n)
'''
N.B.: When you search if something is in a dictionary, 
it is the KEY in the dictionary that is looked for not the value.

for i, num in enumerate(nums):
    dct[i] = num
    if ...:
        return
    else:
        dct[num] = i

The code above is wrong because it adds 2 pairs, a key,value pair and a value,key pair, to the dictionary.
'''

# 2.1.1 Hash table: one pass using range(len())
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target-nums[i]], i]
            else:
                hash[nums[i]] = i
# 57.46%
'''
This solution is later added on 5/10/21.

This solution approves my thinking is correct.
I don't have to rely on "enumerate()" to add to a dictionary.

Wrong code:
def twoSum(nums, target):
    hash = {}
    for i in range(len(nums)):    
        hash[nums[i]] = i
        if target - nums[i] in nums:
            return [hash[nums[i]], nums.index(target-nums[i])]

Fallible mistakes:
1. Remember to check "if ... in hash:" before adding anything to the dictionary.
2. Do not check if it's in "nums", check if is it's in "hash".
3. Do not return the same thing.
'''

# 2.2. Hash table: two pass 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}

        for i in range(len(nums)): # 1st pass
            dct[nums[i]] = i # put number,index as key,value in the dictionary

        for i in range(len(nums)): # 2nd pass
            if target - nums[i] in dct and i != dct[target - nums[i]]: # extra step
                return [i, dct[target - nums[i]]]
# 17.05%
'''
N.B.: Two pass needs an extra step to make sure any number is not counted twice toward the target.
E.g. [3,2,4], 6

N.B.: Two pass approach has 2 for loops, even though the 2 for loops are the same, 
when I tried to combine them, the output is wrong.

I've seen other two pass solutions that also have the extra step
https://leetcode.com/problems/two-sum/discuss/928793/All-three-solutions-in-Python-3

Two pass is written after one pass. I think one pass approach is more intuitive than two pass.
'''

# 3. Two Pointers
# 3.1. Two Pointers with brute force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        nums_s = sorted(nums)
        res = []

        while l < r:
            if nums_s[l] + nums_s[r] > target:
                r -= 1
            
            elif nums_s[l] + nums_s[r] < target:
                l += 1

            else:
                if nums_s[l] != nums_s[r]:
                    return [nums.index(nums_s[l]), nums.index(nums_s[r])]
                
                else:
                    for i in range(len(nums)):
                        if nums[i] == nums_s[l]:
                            res.append(i)    
                    return res
# 16.59%
# This is first successful solution I wrote before trying brute force with 2 for loops.
'''
1. How can I use two pointers if the list is not sorted?
In order to use two pointers, I had to sort the list first.
But as a result, the original order of numbers is lost.
To solve this, I had to go back to the original list and locate each number's index.
But there arises another problem, what if the two numbers are the same?
I then had to add a conditional clause to differentiate the two same numbers by their indexes.

2. There must be a better way to use two pointers for this problem.
'''

# 3.2 Two Pointers


# 4. Binary Search
def twoSum(nums, target):
    '''
    binary_search returns -1 if no target is found
    '''
    nums.sort()
    for i, num in enumerate(nums):
        index = binary_search(target - num, nums)
        if index != -1:
            return [i, index]
'''
This is a binary search solution I copied from Pathrise.

Need to define "binary_search" function first.
'''

# Failed Approaches for Learning Purpose
'''
# Other brute force approaches that I tried but did not work
# None of them was using enumerate() but range(len()) or simple for loop instead
# i. 2 for loops
# This is a generic thought if I choose to go with brute force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
        return res
print(s.twoSum([2,7,11,15], 9)) # -> [0, 1, 1, 0]
# I can't solve Two Sum using two for loops because there will always be another pair

# ii. improvement of i.
# Fix one number and find the next
# Wrote after Hint 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = 1

        for i in range(len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
            
            else:
                j += 1
# This can solve [2,7,11,15], 9; [3,2,4], 6; [3,3], 6; [1,3,4,2], 6; [0,0,1,3,3], 6 but not [3,2,3], 6
# [3,2,3], 6: IndexError: list index out of range
# This doesn't work when the two numbers are not next to each other
# How to improve?

# iii. still 2 for loops
# Inspired to write this after Solution Approach 1
class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            #j = i + 1
            for j in range(1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

s = Solution()
print(s.twoSum([3,3], 6)) # > [0, 1] correct
print(s.twoSum([3,2,3], 6)) # > [0, 2] correct
print(s.twoSum([0,0,1,3,3], 6)) # > [3, 3] wrong 
# But why when the two numbers are beyond nums[0] but adjacent, it outputs two same indexes?
# Because of the for loop. 
# The two for loops overlap after index 0.

# Rewritten iii.:
class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            j = i + 1
            if nums[j] == target - nums[i]:
                return [i, j]
# This is different from the above version, but the same as Brute Force 2 
# because this version outputs [3,3] correctly but reports 'out of range' for [3,2,3] and [0,0,1,3,3]

# In both versions, j is binding to i, meaning they must go pair in pair, 
# j can't be one element away from i.
'''

# Related Topics
'''
1. Array
    - Brute force with enumerate()
2. Hash Table
    - One pass hash table
    - Two pass hash table
'''

# Search problem techniques
'''
1. Sorting and searching

# binary_search returns -1 if no target is found
def twoSum(nums, target):
    nums.sort()
    for i, num in enumerate(nums):
        index = binary_search(target - num, nums)
        if index != -1:
            return [i, index]

2. Hashing
def twoSum(nums, target):
    dic = {}
    for i, num in enumerate(nums):
        if target - num in dic:
            return [i, dic[target - num]]
        dic[num] = i
'''

# Similar Questions
'''
3Sum Medium
4Sum Medium
Two Sum II - Input array is sorted Easy
Two Sum III - Data structure design Easy
Subarray Sum Equals K Medium
Two Sum IV - Input is a BST Easy
Two Sum Less Than K Easy
Max Number of K-Sum Pairs Medium
Count Good Meals Medium
'''

# Test Cases
'''
[2,7,11,15]
9
[3,2,4]
6
[3,3]
6
[3,2,3]
6
[1,3,4,2]
6
[0,0,1,3,3]
6
'''
s = Solution()
print(s.twoSum([2,7,11,15], 9)) #> [0,1]
print(s.twoSum([3,2,4], 6)) #> [1,2]
print(s.twoSum([3,3], 6)) #> [0,1]
print(s.twoSum([3,2,3], 6)) #> [0,2]
print(s.twoSum([1,3,4,2], 6)) #> [2,3]
print(s.twoSum([0,0,1,3,3], 6)) #> [3,4]