# 1446. Consecutive Characters
# Easy


# my wronged-many-times solution using stack, pay ATTENTION to edge cases
class Solution:
    def maxPower(self, s: str) -> int:
        s = list(s)
        stack = []
        ans = 1
        
        for _ in s:
            if _ not in stack:
                stack = [_]
            else:
                stack.append(_)
                ans = max(ans, len(stack))
        
        return ans
# Runtime: 36 ms, faster than 93.39%
# Memory Usage: 14.3 MB, less than 12.90%
# time O(n), traverse once 
# space O(n), maximum all elements in the array
# N.B. remember to update ans not just set ans 
# ans = max(ans, len(stack))


# ----------------------

# two pointers?
class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        s = list(s)
        l, r = 0, 1
        ans = temp = 1
        
        while r < len(s):
            if s[l] != s[r]:
                temp = 1
                l = r
                r += 1
            else:
                temp = r - l + 1
                ans = max(ans, temp)
                r += 1
        
        return ans
# Runtime: 48 ms, faster than 43.63%
# time O(n)
# space O(1)
# N.B. ans will keep updating throughout the array, 
# so we need to have a temp to make sure 
# ans only takes in max


# ----------------------

# lc solution
class Solution:
    def maxPower(self, s: str) -> int:
        count = 0
        max_count = 0
        previous = None
        for c in s:
            if c == previous:
                # if same as previous one, increase the count
                count += 1
            else:
                # else, reset the count
                previous = c
                count = 1
            max_count = max(max_count, count)
        return max_count
# previous set to None instead of using two pointers