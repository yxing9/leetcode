# 849. Maximize Distance to Closest Person
# Medium


# Larry's https://www.youtube.com/watch?v=fnTKu-Q0g9Q
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        seats = collections.deque((t, len(list(items))) for t, items in groupby(seats))
        best = 0
        
        # We start with empty seats
        if len(seats) > 0 and seats[0][0] == 0:
            best = max(best, seats[0][1])
        # We end with empty seats
        if len(seats) > 0 and seats[-1][0] == 0:
            best = max(best, seats[-1][1])
            
        for t, c in seats:
            if t == 0:
                best = max(best, (c + 1) // 2)
                
        return best
# 01/16/2022 18:46



# --- END --- #