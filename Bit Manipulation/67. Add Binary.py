# 67. Add Binary
# Easy
# Bit Manipulation



# my naive solution
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dec_a = self.getDecimal(a)
        dec_b = self.getDecimal(b)
        temp = dec_a + dec_b
        if temp == 0:
            return "0"
        else:
            res = self.getBinary(temp)
            return res
    
    def getDecimal(self, bi):
        s = str(bi)
        temp = list(s)
        n = len(temp)
        res = 0
        for i in range(n):
            res += int(temp[i]) * (2 ** (n-1-i))
        return res
    
    
    def getBinary(self, dec):
        res = ''
        while dec > 0:
            quotient = dec // 2
            reminder = dec % 2
            res = str(reminder) + res
            dec = quotient
        return res
# 01/09/2022 19:34
# Is time and space complexity both O(1)?
# Note that the result returned by getBinary() is str, not int since the question requires str, 
# but the getDecimal() returns <class 'int'> 
# It's a proof that my naive thought process works, so I am happy. 
# But there is a bug in my 476 code. What used in 67 is correct. 


# I am skipping the bit manipulation solution. 



# --- End --- #