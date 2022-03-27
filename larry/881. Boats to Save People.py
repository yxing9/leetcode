# 881. Boats to Save People
# Medium

# Larry, https://www.youtube.com/watch?v=rmjUVepmN8o
from sortedcontainers import SortedList

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        sl = SortedList(people, key=lambda x: -x)
        
        while len(sl) > 0:
            item = sl[0]
            sl.remove(item)
            
            index = sl.bisect_left(limit - item)
            if index < len(sl):
                sl.remove(sl[index])
                
            boats += 1
        return boats
# 03/24/2022 19:01