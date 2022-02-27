# 258. Add Digits
# Easy






class Solution:
    def addDigits(self, num: int) -> int:
        
        def helper(num):
            num = list(str(num))
            temp = 0
            if len(num) == 1:
                return num[0]
            else:
                for i in num:
                    temp += int(i)
                num = temp
                helper(num)
        
        return helper(num)
s = Solution()
print(s.addDigits(38))
# why this returns none?



# Larry
class Solution:
    def addDigits(self, num: int) -> int:
        """
        # Larry, https://www.youtube.com/watch?v=FRWUcc1cX9A
        """
        if num == 0:
            return num
        digit = num % 9
        if digit == 0:
            digit = 9
        return digit