# 29. Divide Two Integers
# M


# Larry, https://www.youtube.com/watch?v=82qk_F-djUw
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = True
        if (dividend > 0) != (divisor > 0):
            positive = False
            
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend < divisor:
            return 0
        
        ans = 0
        left = dividend
        
        # Return two things - the remainder, and a number b such that
        # b is the biggest number that is a power of 2
        # b * divisor < left
        # O(R)
        def find(left, divisor):
            current = divisor
            b = 1
            
            while current + current <= left:
                current += current
                b += b
                
            # print(left, divisor, left - current, b)
            return left - current, b
        
        # R = the number of bits in the dividend
        # log N = R
        # O(R) loops
        # total time -> O(R^2) -> O(log^2 N)
        # total space -> linear -> O(R)
        while left >= divisor:
            left, b = find(left, divisor)
            ans += b
            
        if positive:
            return min(ans, (1 << 31) - 1)
        else:
            return max(-ans, -(1 << 31))
# 05/30/2022 15:03