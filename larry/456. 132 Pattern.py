# 456. 132 Pattern
# Medium


# Larry, https://www.youtube.com/watch?v=y0adBCWCHTI
from sortedcontainers import SortedList

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        INF = 10 ** 20
        mn = INF
        
        prefix = [INF]
        for x in nums:
            prefix.append(min(prefix[-1], x))
            
        suffix = [INF]
        sl = SortedList()
        
        for x in nums[::-1]:
            index = sl.bisect_left(x)
            if index - 1 >= 0:
                suffix.append(sl[index - 1])
            else:
                suffix.append(-INF)
            sl.add(x)
        suffix.reverse()
        
        for p, x, s in zip(prefix[1:], nums, suffix[:-1]):
            if p < s:
                #print(p, x, s)
                return True
        return False
# 05/07/2022 01:49