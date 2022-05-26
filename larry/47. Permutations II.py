# 47. Permutations II
# M


# Larry, https://www.youtube.com/watch?v=iSo_0bewK-I
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        N = len(nums)
        ans = []
        
        used = [False] * N
        
        """
        1,1,1,2,3,3,4
        ^ ^
        """
        
        def recurse(current):
            if len(current) == N:
                ans.append(current[:])
                return
            
            for i in range(N):
                if not used[i] and (i == 0 or nums[i] != nums[i - 1] or used[i - 1]):
                    used[i] = True
                    current.append(nums[i])
                    recurse(current)
                    current.pop()
                    used[i] = False
                    
        recurse([])
        return ans
# 05/12/2022 17:13