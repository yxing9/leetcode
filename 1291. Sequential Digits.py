# 1291. Sequential Digits
# Medium
# Enumeration


'''

an array problem?


my first attempt:
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        temp = []
        low_str = str(low)
        N = len(low_str)
        start = low_str[0]
        
        for i in range(N):
            temp.append(start + i)

problem with this attemp:
e.g. low = 1000, high = 13000
1. can't switch to startswith 2 after done with 1
2. don't know how to expand to high.length after done with low.length


'''


# larry 1, https://www.youtube.com/watch?v=vLJjEwaFRrE
# me, cosmetic change
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def gen(digit, current):
            ans = []
            
            current *= 10
            current += digit
            
            if low <= current <= high:
                ans.append(current)
            
            if digit < 9:
                ans += gen(digit + 1, current)
            
            return ans
        
        ans = []
        for i in range(1, 10):
            ans += gen(i, 0)
        
        ans.sort()
        
        return ans
# 01/24/2022 20:24


# larry 2, same link as above
# I perfer this, cleaner
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        
        def gen(digit, current):
            current *= 10
            current += digit
            
            if low <= current <= high:
                ans.append(current)
            
            if digit < 9:
                gen(digit + 1, current)
            
        for i in range(1, 10):
            gen(i, 0)
            
        ans.sort()
        
        return ans
# 01/24/2022 20:34
# constant because the number of digits is constant
# But if you have a different base, B for base
# B is the base of digits, e.g. 10 digits is base 10
# then B^2 total numbers
# time O(B^2)
# space O(B^2)



# There is another different solution in the video but I skipped copying it here.



# --- END --- #