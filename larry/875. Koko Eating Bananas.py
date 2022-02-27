# 875. Koko Eating Bananas
# Medium



'''

1. sum(piles) / piles.length and h
2. piles.length and h


if piles.length == h:
    k = max(piles)


min value of k is sum(piles) / piles.length
max value of k is max(piles)


------

I had no idea it was binary search until I saw Related Topics



'''


# Larry, https://www.youtube.com/watch?v=Nf2J7sJOXpo
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isEatingSpeedEnough(speed):
            if speed == 0:
                return False
            
            days = 0
            
            for x in piles:
                days += (x + speed - 1) // speed
                
            return days <= h
        
        left = 0
        right = 10 ** 13 + 5
        
        while left < right:
            mid = (left + right) // 2
            
            if isEatingSpeedEnough(mid):
                right = mid
            else:
                left = mid + 1
                
        return left