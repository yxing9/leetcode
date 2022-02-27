# 605. Can Place Flowers
# Easy
# Greedy


'''

Edge cases:

flowerbed.length 1, 2

my initial thought was to compare [i-1] [i] [i+1]

later i thought of sliding window

but it's a greedy problem

'''


# Larry's, 
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        N = len(flowerbed)
        count = 0
        
        previous = False
        for i in range(N):
            if flowerbed[i] == 1:
                previous = False
                continue
            if i - 1 >= 0 and (flowerbed[i - 1] == 1 or previous):
                previous = False
                continue
            if i + 1 < N and flowerbed[i + 1] == 1:
                previous = False
                continue
                
            count += 1
            previous = True
            
        return count >= n
# 01/18/2022 18:44



# --- END --- #