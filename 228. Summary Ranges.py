# 228. Summary Ranges
# Easy


# Larry, https://www.youtube.com/watch?v=xcwnOzyoNII
# implementation problem
# slightly modified
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        N = len(nums)
        if N == 0:
            return []
        
        INF = 10 ** 10
        nums.append(INF)
        ans = []
        startpoint = nums[0]
        
        for i in range(N):
            if nums[i + 1] != nums[i] + 1:
                endpoint = nums[i]
                
                if endpoint == startpoint:
                    ans.append(f"{startpoint}")
                else:
                    ans.append(f"{startpoint}->{endpoint}")
                    
                startpoint = nums[i + 1]
                endpoint = None
        
        return ans
# 02/28/2022 17:40
# Why "if nums[i + 1] != nums[i] + 1" does not have a "out of range" error?
# Because we set N = nums.length before appending INF to nums, 
# i is thus confined in the range of original elements, 
# i+1 is also valid because it's INF.


# my initial try
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        temp = []
        ans = []
        N = len(nums)
        for i in range(N - 1):
            temp.append(nums[i])
            if nums[i + 1] != nums[i] + 1 and nums[i] not in temp:
                temp.append(nums[i])
            ans.append(temp)
        return ans



# --- END --- #