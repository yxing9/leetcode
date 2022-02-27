# 312. Burst Balloons
# Hard


'''

dp

[3,1,5,8]

          3                      1                 5                 8
    /     |     \          /     |     \
   1      5      8        3      5      8
  / \    / \    / \      / \    / \    / \
 5   8  1   8  1   5    5   8  3   8  3   5
 |   |  |   |  |   |    |   |  |   |  |   |
 8   5  8   1  5   1    8   5  8   3  5   3

 3158 3185 ......

n to the power of n



NeetCode
pop it last, instead of pop it first




'''


# NeetCode's O(n3) time and O(n2) space solution -> TLE
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        '''
        NeetCode solution
        '''
        nums = [1] + nums + [1]
        dp = {}
        
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]
        
        return dfs(1, len(nums) - 2)


# Another lc discuss solution, link below
class Solution(object):
    def maxCoins(self, nums):
        '''
        https://leetcode.com/problems/burst-balloons/discuss/1659527/C%2B%2BPythonJava-2-Simple-Solutions-oror-DP-and-Recursion-oror-Detailed-Explanation
        '''
        nums = [1] + nums + [1]  # add the dummy head and tail, both are left till end and DO NOT burst them.
        mem = collections.defaultdict(int)  # standard memory trick to avoid repeated function calculations

        def search(nums):
            if tuple(nums) in mem:  # standard memory trick to avoid repeated function calculations
                return mem[tuple(nums)]
            ans = [0] * len(nums)
            # try each balloon except the head and tail to leave it till the end, note that head and tail are defined
            # to leave as the last two balloons, so nums[i] is actual the third from last, and at last we burst nums[i],
            # and get head * nums[i] * tail, finally we choose the one which can get the maximum coins.
            # the head and tail are busted in outer recursive function if they are not dummy, so if len(nums) < 3, 
            # return 0.
            for i in range(1, len(nums) - 1):
                ans[i] = search(nums[:i + 1]) + search(nums[i:]) + nums[0] * nums[i] * nums[-1]
            mem[tuple(nums)] = max(ans)
            return mem[tuple(nums)]

        return search(nums)