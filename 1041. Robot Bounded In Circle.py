# 1041. Robot Bounded In Circle
# Medium
#
# mostly asked by Amazon in 2021

'''

How to determine it's a circle?

isNotCircle:
all G's is no circle, like GG
GLR
GRL

isCircle:
anything no G is circle, like LLL, RRR, LLR, RRL
GL
GGLL
GGLLGG


I am trying to find a pattern...

no:
LRLR
LLRR

yes:


----

after Hint 1:
G = 1
L = 
R = 

calculate start and end, check if they are equal


----
Why not just put them in a coordinate?

----

NeetCode

- change in position
    - still at origin -> return True
    - or at another position -> it depends
- change in direction
    - still facing north -> return False
    - or direction changed -> return True

(because if it's still facing north, no matter how many times we run the instruction, 
it's gonna be facing north)

(but if the direction changes, 
no matter if it changes by one, from north to east or west, 
or by two, from north to south, 
we can ensure it runs in circle after 4 or 2 times of repeating the instruction)

we can return true if the direction changes at least by one direction


'''



# NeetCode, https://www.youtube.com/watch?v=nKv2LnC_g6E
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0 # starting point is the origin
        dx, dy = 0, 1 # starting point is north-facing
        
        for d in instructions:
            if d == "G":
                x, y = x + dx, y + dy
            elif d == "L":
                dx, dy = -dy, dx
            elif d == "R":
                dx, dy = dy, -dx
                
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)
# time O(n) for iterating the instructions
# space O(1)
# ----
# dx, dy = -dy, dx is from linear algebra
# intuition for L & dx = -dy: ^ to <
# intuition for R & dy = -dx: > to down
# Now I fully understand this solutiuon.
# ----
# NeetCode said it's not easy to come up with a readable code like this
# but I feel this is very clear to understand. 



# --- End --- #