# 565. Array Nesting
# Medium


from typing import List


# DFS
# https://leetcode.com/problems/array-nesting/discuss/1438313/C%2B%2BPython-Find-the-longest-length-between-cycles-with-Picture-Clean-and-Concise
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False] * n
        ans = 0
        for x in nums:
            cnt = 0
            while not visited[x]:
                cnt += 1
                visited[x] = True
                x = nums[x]
            ans = max(ans, cnt)
        return ans



# DP Memo that almost worked
# Couln't solve it using dp memoization
# class Solution:
#     def arrayNesting(self, nums: List[int]) -> int:
#         return self.arrayNestingRec(nums, 0, [])

#     def arrayNestingRec(self, nums, i, s):
#         if nums[i] in s:
#             return len(s)
#         s.append(nums[i])
#         self.arrayNestingRec(nums, nums[i], s)
#         return len(s), s
# It cannot handle nums that starts with 0 and not always increasing,
# like [0,2,1] and [0,1,2,4,3] etc.



s = Solution()
print(s.arrayNesting([5,4,0,3,1,6,2])) # expect 4
print(s.arrayNesting([0,1,2])) # expect 1
print(s.arrayNesting([0,2,1])) # expect 2

'''
make sure the last element you get is the index that you start.
like S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}, you can find S[0] = {5, 6, 2, 0}
'''