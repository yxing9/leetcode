# 1342. Number of Steps to Reduce a Number to Zero
# E


# Larry, https://www.youtube.com/watch?v=RiIClSeHwiE
class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            steps += 1
        
        return steps
# 05/26/2022 22:35
# O(n) time, n is the input number
# O(log n) space


# My solution
class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        
        if num == 0:
            return ans
        
        while num > 0:
            if num % 2 == 0:
                num = num / 2
                ans += 1
            else:
                num -= 1
                ans += 1
        
        return ans
# 05/26/2022 22:25