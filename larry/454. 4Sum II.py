# 454. 4Sum II
# Medium


# Larry's, https://www.youtube.com/watch?v=NADrbTvDYuk
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        lookup = collections.Counter()
        
        # O(N^2) time and space
        for x in nums1:
            for y in nums2:
                lookup[x + y] += 1
                
        total = 0
        for x in nums3:
            for y in nums4:
                total += lookup[-(x + y)]
        return total




# --- END --- #