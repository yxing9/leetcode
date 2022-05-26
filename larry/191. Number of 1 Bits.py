# 191. Number of 1 Bits
# E


# Larry, https://www.youtube.com/watch?v=dZS4UdxJrv8
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while n > 0:
            count += (n & 1)
            n >>= 1
            
        return count
# 05/26/2022 15:05