# 1679. Max Number of K-Sum Pairs
# Medium


# Larry, https://www.youtube.com/watch?v=-LY5OzAGLV0
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = collections.Counter(nums)
        
        pairs = 0
        for key in freq.keys():
            a, b = key, k - key
            if a > b:
                pairs += min(freq[a], freq[b])
            elif a == b:
                pairs += freq[a] // 2
        return pairs
# 05/04/2022 16:29