# 695. Max Area of Island


'''

one key difference from 200 is that 
in the two for loops traversing each element phase, 
in 695 we don't need to check if an element is an island, 
but in 200 we do need to check that.


where i was stuck:
i didn't know how to calculate the area. 
it's actually very easy, 
just to add the four directions, 
dfs(r+1,c) and so on, 
plus 1, which is itself


a small optimization: 
if the input grid is overwritable, 
we can overwrite the input grid 
to save space on the external hash set.

'''


# neetcode
# 11/24
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        '''
        
        process visited in dfs instead of the root function
        
        '''
        def dfs(r, c):
            
            #if r in range(row) and c in range(col) and grid[r][c] == 1 and (r,c) not in visited:
            if r < 0 or r == row or c < 0 or c == col or grid[r][c] == 0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            return (1 + dfs(r+1, c) + 
                        dfs(r-1, c) + 
                        dfs(r, c+1) + 
                        dfs(r, c-1))
        
        row = len(grid)
        col = len(grid[0])
        visited = set()
        area = 0
        for r in range(row):
            for c in range(col):
                area = max(area, dfs(r, c))
        
        return area
# Runtime: 156 ms, faster than 45.39%
# time: O(m * n) for each element
# space: O(m * n) for the hash set
# follow-up: can i put visited in the root func?


# refactor a little
# same as above, just added if in visited in the root func
# 11/24
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        '''
        
        follow up on previous solution
        i can put 'if in visited' in the root func, 
        but i can't take 'if in visited' off dfs func,
        because dfs will expand to other elements 
        that might not be visited yet
        
        '''
        def dfs(r, c):
            
            if r < 0 or r == row or c < 0 or c == col or grid[r][c] == 0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            return (1 + dfs(r+1, c) + 
                        dfs(r-1, c) + 
                        dfs(r, c+1) + 
                        dfs(r, c-1))
        
        row = len(grid)
        col = len(grid[0])
        visited = set()
        area = 0
        for r in range(row):
            for c in range(col):
                if (r,c) not in visited: # optional
                    area = max(area, dfs(r, c))
        
        return area
# Runtime: 196 ms, faster than 20.83%
# doesn't seem to be faster so it's totally optional, better without it