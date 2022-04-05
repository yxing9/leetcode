# 31. Next Permutation
# Medium



# Larry, https://www.youtube.com/watch?v=NydoSm661fM
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start, end):
            j = end
            for i in range(start, end + 1):
                if i >= j:
                    break
                    
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            
        N = len(nums)
        i = N -1
            
        while i >= 1 and nums[i - 1] >= nums[i]:
            i -= 1
            
        if i == 0:
            reverse(0, N - 1)
            return
            
        digit = i - 1
        i = N - 1
        while i > digit and nums[i] <= nums[digit]:
            i -= 1
            
        if i == digit:
            reverse(digit, N - 1)
            return
            
        nums[i], nums[digit] = nums[digit], nums[i]
        reverse(digit + 1, N - 1)
# 04/03/2022 17:50