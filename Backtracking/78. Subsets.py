# 78. Subsets
# Medium
# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums):
        def backtracking(picked, i, nums):
            if i == len(nums):
                res.append(picked)
            else: 
                backtracking(picked + [nums[i]], i+1, nums)
                backtracking(picked, i+1, nums)
        res = []
        backtracking([], 0, nums)
        return res
# 54.86%
'''
Modified based on Pathrise's solution below:

def subsets(L):
    backtracking([], 0, L)

def backtracking(picked, i, L):
    if i == len(L):
        print(picked)
    else: 
        backtracking(picked + [L[i]], i+1, L)
        backtracking(picked, i+1, L)
'''

s = Solution()
print(s.subsets([1,2,3]))