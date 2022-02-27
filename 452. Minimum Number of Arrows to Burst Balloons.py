# 452. Minimum Number of Arrows to Burst Balloons
# Medium
# Array
# Greedy
# Sorting



'''

1. Do I need to sort the array first?

[[10,16],[2,8],[1,6],[7,12]]
[[1,6],[2,8],[7,12],[10,16]]

1....6
 2.....8
      7....12
         10........16

2 arrows

 7 is within 8   but not within 6
10 is within 12  but not within 8

feel like it's sliding window


1. sort the array
2. create a l and r sliding window
3. count how many windows there are after traversing the entire array


find the common subset, smallest

----------

Larry's
sweep line + greedy

greedy:
don't fire the arrow unless you absolutely have to, 
meaning if you are missing a balloon, you have to fire

once a balloon is shot, we don't have to care about that balloon anymore 



------

I AM CONFUSED



'''


# Larry's 1
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # O(N) space
        # O(N log N) time
        N = len(points)
        events = []
        START = -1
        END = 1

        for i, (s, e) in enumerate(points):
            events.append((s, START, i))
            events.append((e, END, i))

        events.sort()

        count = 0
        done = [False] * N
        # a list of "current" ballons within range
        # O(N) time
        current = []
        for x, e, i in events:
            if e == START:
                current.append(i)
            else:
                assert(e == END)

                if done[i]:
                    continue

                # we have to shoot this balloon, and everything that is in "current" will be popped
                for ci in current:
                    done[ci] = True
                # without this below, the complexity is now O(N^2)
                current = []
                count += 1
        
        return count
# 01/13/2022 16:30

# Larry's 1 year 3 months ago solution
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        events = []
        for index, (bottom, top) in enumerate(points):
            events.append((bottom, +1, index))
            events.append((top, -1, index))

        events.sort(key=lambda x:(x[0], -x[1]))

        count = 0
        in_set = set()
        done = set()

        for x, delta, index in events:
            if delta == 1:
                in_set.add(index)
            
            if delta == -1 and index not in done:
                count += 1
                done |= in_set

        return count
# 01/13/2022 16:34

# --------

# I stopped trying 
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        l, r = points[0][0], points[0][1]
        windows = []
        
        for i in range(1, n):
            if l <= points[i][0]: # l becomes the bigger one
                l = points[i][0]
            if r >= points[i][1]: # r becomes the smaller one
                r = points[i][1]
            if not windows:
                windows.append([l,r])
            # elif l >= windows[-1][0] and r <= windows[-1][1]:
                
                
                
        # for start, end in points:
            
        
        # return windows




# --- End --- #