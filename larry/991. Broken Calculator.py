# 991. Broken Calculator
# Medium


# Larry, https://www.youtube.com/watch?v=gg7CPdQ7yQM
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0
        while startValue < target:
            if target % 2 == 1:
                target += 1
                target //= 2
                count += 2
            else:
                target //= 2
                count += 1
                
        return count + startValue - target