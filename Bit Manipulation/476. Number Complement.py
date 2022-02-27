# 476. Number Complement
# Easy
# bit manipulation
# 1009. Complement of Base 10 Integer


# my initial solution - failed
class Solution:
    def findComplement(self, num: int) -> int:
        
        def getBinaryFromDecimal(decimal_num):
            res = 0
            while decimal_num > 0:
                quotient = decimal_num // 2
                reminder = decimal_num % 2
                res = res * 10 + reminder
                decimal_num = quotient
            return res
            
        
        def getDecimalFromBinary(binary_num):
            s = str(binary_num)
            temp = list(s)
            n = len(temp)
            res = 0
            for i in range(n):
                res += int(temp[i]) * (2 ** (n-1-i))
            return res
        
        
        binary = getBinaryFromDecimal(num)
        complement = ~binary #+ 1 # ~ to reverse bit then +1 to get complement
        # decimal = getDecimalFromBinary(complement)
        
        return complement



# lc solutions
# XOR of zero and a bit results in that bit
# 4 approaches
# Approach 1: Flip Bit by Bit
# I wrote after seeing the solution
class Solution:
    def findComplement(self, num: int) -> int:
        todo, bit = num, 1
        while todo:
            num = num ^ bit
            todo = todo >> 1
            bit = bit << 1
        return num
# Runtime: 24 ms, faster than 94.84% 



# --- End --- #