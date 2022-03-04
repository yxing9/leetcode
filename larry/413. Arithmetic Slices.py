# 413. Arithmetic Slices
# Medium


# Larry, https://www.youtube.com/watch?v=RzubwvvmhKc
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        [1,2,3,4]
        
        [1,2,3] -> 1 subarray
        [1,2,3,4] -> length of 4 means -> 1 subarray of length 3, and 1 subarray of length 4
        [1,2,3,4,5] -> length of 5 means -> 1 subarray of length 3, 1 subarray of length 4, and 1 subarray of length 5
        """
        
        total = 0
        streak = 2
        lastDelta = None
        
        N = len(nums)
        
        for i in range(N - 1):
            prev, current = nums[i], nums[i + 1]
            
            delta = current - prev
            
            if lastDelta == delta:
                streak += 1
            else:
                streak = 2
                lastDelta = delta
                
            total += max(streak - 2, 0)
            
        return total
# 03/03/2022 17:48