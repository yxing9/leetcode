# 231. Power of Two
# Easy


'''

            
        # if n % 2 == 0:
        #     return True
        # else:
        #     return False
        

A great little question to practice math, 
floor division, modulo, and edge case awareness.

'''


# my solution 12/20/2021
# the oblivious O(log n) solution per lc
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False 
        
        if n > 0 and n <= 2:
            return True 
        
        while n > 2:
            n = n / 2

        return (n % 2 == 0)
# Runtime: 28 ms, faster than 88.11%
# time O(log n) for halving every time 
# space O(1)

# lc solution
class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1
# very well written

# ----

# Bit Manipulation on lc
# Approach 1: Bitwise Operators : Get the Rightmost 1-bit
class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (-n) == n
'''

Complexity Analysis

Time complexity : \mathcal{O}(1)O(1).

Space complexity : \mathcal{O}(1)O(1).

'''
# Approach 2: Bitwise operators : Turn off the Rightmost 1-bit
class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (n - 1) == 0
'''

Complexity Analysis

Time complexity : \mathcal{O}(1)O(1).

Space complexity : \mathcal{O}(1)O(1).

'''


# --- End --- #