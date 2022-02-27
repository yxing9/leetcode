# 46. Permutations

class Solution:
    def permute(self, nums):
        def backtracking(perm, nums):
            if len(perm) == len(nums):
                res.append(perm)
            for num in nums:
                if num not in perm:
                    backtracking(perm+[num], nums)
        res = []
        backtracking([], nums)
        return res
# 38.41%
'''
Pathrise's Permutations solution:

def permutations(nums):
    backtracking([], nums)
def backtracking(perm, nums):
    if len(perm) == len(nums):
        print(perm)
        return
    for num in nums:
        if not num in perm:
            backtracking(perm+[num], nums)


Same
if num not in perm:
if not num in perm:
'''

s = Solution()
print(s.permute([1,2,3]))