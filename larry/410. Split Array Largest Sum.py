# 410. Split Array Largest Sum
# Hard


# Larry, https://www.youtube.com/watch?v=CgB7SHuhBaA
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = 0
        right = sum(nums)
        
        # given the max sum of a subarray is "target", how many subarrays are there
        # (and is that number smaller than or equal "m")
        def good(target):
            count = 1
            current = 0
            
            for x in nums:
                if x > target:
                    return False
                
                current += x
                if current > target:
                    count += 1
                    current = x
                
            return count <= m
        
        # R = 10 ** 6 * 1000 -> 10 ** 9
        # log(R) ~ 30 iterations
        while left < right:
            mid = (left + right) // 2
            
            # O(N)
            if good(mid):
                right = mid
            else:
                left = mid + 1
                
        # O(N log R) time
        # O(1) space
        return left
# 03/31/2022 19:42