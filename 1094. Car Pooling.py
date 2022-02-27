# 1094. Car Pooling
# Medium
# Difference Array, Sweep Line
# Sorting
# Simulation

'''

sweep line
https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/discuss/854206/JavaC%2B%2BPython-Sweep-Line

More Sweep Line Problems

253. Meeting Rooms II
1094. Car Pooling
1109. Corporate Flight Bookings


Difference Array. Below are similar problems.

1893 Check if All the Integers in a Range Are Covered
370 Range Addition
1381 Design a Stack With Increment Operation
2021 Brightest Position on Street
1094 Car Pooling

'''

'''

[[2,1,5],[3,3,7]]   4

    1---5--     2
    --3---7     3

    trip[i][0], trip[i][1], trip[i][2]
    
    if      5     >     3       :
    if trip[i][2] > trip[i+1][1]: then we need to check if within capacity
        if trip[i][0] + trip[i] >= capacity: 
            return False

Logic:
1. check if numPassenger is greater than capacity, if not continue
2. check if 1st to is earlier or later than 2nd from 
   if earier, all good 
   if later, check if 1st numPassenger + 2nd numPassenger exceed capacity


------

Larry's solution:
simulation problem
events: split into two events:
    people getting in event
    people getting off event

p, s, e
passenger, start, end

t, e, delta
time, event, delta

for t, e, delta:
    if e == ON:
        # do ON stuff
    if e == OFF:
        # do OFF stuff


----

LC Approaches:

1. time stamp
    - this is actually larry's solution 
2. bucket sort
    - 0 <= trips[i][1] < trips[i][2] <= 1000
    - 0 <= fromi < toi <= 1000
    - this constraint hints bucket sort
    - use bucket sort when you know there are specific number of buckets, 
        - in this case stops fromi and toi


'''



# Larry's simulation and event solution
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        Larry's solution, https://www.youtube.com/watch?v=-TtHUNoqWv8
        time O(nlogn)
        space O(n)
        '''
        events = []
        
        OFF = 0
        ON = 1
        
        for p, s, e in trips:
            events.append((s, ON, p))
            events.append((e, OFF, -p))
            
        events.sort()
        
        current = 0
        
        for t, e, delta in events:
            current += delta
            
            if current > capacity:
                return False
            
        return True
# 01/06/2022 18:25
# ON and OFF is not necessary for this particular question, he already said that. 


# my practice
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        practice
        '''
        events = []
        
        on = 1
        off = 0
        
        for p, s, e in trips:
            events.append([s, on, p])
            events.append([e, off, -p])
            
        events.sort()
        
        count = 0
        
        for i, j, p in events:
            count += p
            if count > capacity:
                return False
            
        return True
# 01/06/2022 22:33
# Larry used tuple, he mentioned we can use name tuple
# but i tried that () can be []


# ----


# LC solution: time stamp
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        LC timestamp solution
        I wrote and changed the variable name from time to status.
        '''
        timestamp = []
        for trip in trips:
            timestamp.append([trip[1], trip[0]])
            timestamp.append([trip[2], -trip[0]])
            
        timestamp.sort()
        
        used_capacity = 0
        for status, passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False
            
        return True
# 01/10/2022 13:17
# time O(n log n) for sorting
# space O(n) for storing timestamp[] in the worst case


# ----


# LC solution: bucket sort
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        LC bucket sort solution
        '''
        timestamp = [0] * 1001
        for trip in trips:
            timestamp[trip[1]] += trip[0] # note +=
            timestamp[trip[2]] -= trip[0] # note -=, and positive trip[0]
        
        used_capacity = 0
        for passenger_change in timestamp: # don't have to sort timestamp
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False
            
        return True
# 01/10/2022 18:00




# --- End --- #