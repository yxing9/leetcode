# 509. Fibonacci Number
# Easy
# https://leetcode.com/problems/fibonacci-number/

'''

3 solusions:

recursion
dynamic programming memorization, top down
dynamic programming tabulation, bottom up

'''


# dp tabulation
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        arr = [0, 1] + [0]*(n-1)
        for i in range(2, n+1):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[-1]
# or, Pathrise Jason Filippou's version
# Is it more academic?
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            arr = [0, 1] + [0]*(n-1)
            for i in range(2, n+1):
                arr[i] = arr[i-1] + arr[i-2]
            return arr[-1]





# Recursion -> 07182021
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1: # n <= 1
            return n
        return self.fib(n-1) + self.fib(n-2)
# time: O(2^n)
# space: O(n)


# DP Memo Top Down -> 07262021
class Solution:
    def fib(self, n: int, memo={}) -> int:
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = self.fib(n-1, memo) + self.fib(n-2, memo)
        return memo[n]
# time: O(n)
# space: O(n)


# DP Tabulation Bottom Up -> 07262021
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        x, y = 0, 1
        i = 2
        while i < n:
            temp = x + y
            x = y
            y = temp
            i += 1
        return x + y
# time: O(n)
# space: O(1)
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        fib_minus_2 = 0
        fib_minus_1 = 1
        for _ in range(1, n):
            temp = fib_minus_2 + fib_minus_1
            fib_minus_2 = fib_minus_1
            fib_minus_1 = temp
        return temp
# Note that here we are returning temp but not x + y. Why?
# Because we are starting from 1.
# If we are starting from 2, shown as below, 
# we will return the same as in x + y.
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        fib_minus_2 = 0
        fib_minus_1 = 1
        for _ in range(2, n):
            temp = fib_minus_2 + fib_minus_1
            fib_minus_2 = fib_minus_1
            fib_minus_1 = temp
        return fib_minus_2 + fib_minus_1
# Runtime: 20 ms, faster than 99.12% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 14.3 MB, less than 8.57% of Python3 online submissions for Fibonacci Number.


s = Solution()
print(s.fib(2)) # expect 1
print(s.fib(3)) # expect 2
print(s.fib(4)) # expect 3
print(s.fib(5)) # expect 5
print(s.fib(6)) # expect 8