# 463. Island Perimeter
# bfs but not actually

'''

I came up with a solution, solution 1: 
count the total # of sides horizontally, 
 plus the total # of sides vertically,
we have the final answer.
but don't know how to implement it.

------

after lc discuss

solution 2: ans = #islands * 4 - #neighbors * 2
i don't have to get #islands like in 695, 
i can just iterate the entire grid to find #islands, 
because in 695 there are more than 1 piece of island.


11/29
No need to use bfs in this question, a one-by-one traversal 
is enough to solve the question. 


solution 3:
everytime when hit a boundary or water, +1


solution 4: by gatsby7d
https://leetcode.com/problems/island-perimeter/discuss/95007/Short-Python


'''

# solution 2
# based on https://leetcode.com/problems/island-perimeter/discuss/95001/clear-and-easy-java-solution
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        area = 0
        neighbors = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area += 1
                    if i+1 < rows and grid[i+1][j] == 1:
                        neighbors += 1
                    if j+1 < cols and grid[i][j+1] == 1:
                        neighbors += 1
        ans = 4 * area - 2 * neighbors
        return ans
# Runtime: 456 ms, faster than 97.07%
# time O(m * n) m is #rows of grid, n is #cols of grid
# space O(1)



# solution 3: counting boundaries and water cells
# idea inspired in lc discuss, code by me
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    if i == 0: # boundary: first row
                        perimeter += 1
                    if i == rows-1: # boundary: last row
                        perimeter += 1
                    if j == 0: # boundary: first column
                        perimeter += 1
                    if j == cols-1: # boundary: last column
                        perimeter += 1
                    if i+1 in range(rows) and grid[i+1][j] != 1: # cell below it is water
                        perimeter += 1
                    if i-1 in range(rows) and grid[i-1][j] != 1: # cell above it is water
                        perimeter += 1
                    if j+1 in range(cols) and grid[i][j+1] != 1: # cell right to it is water
                        perimeter += 1
                    if j-1 in range(cols) and grid[i][j-1] != 1: # cell left to it is water
                        perimeter += 1
        return perimeter
# Runtime: 596 ms, faster than 62.98%
# time O(m * n)
# space O(1)


# -------------------

# wrong solution
from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        '''
        
        wrong answer to the question

        but why directly assign dfs(r,c) to area won't work as max() ?
        
        updated on 11/29  
        Because in area = dfs(r,c), area is never locked when it hits the max area, 
        instead area constantly changes until the last (r,c)
        
        '''

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or grid[r][c] != 1:
                return 0
            visited.add((r,c))
            return (1 + dfs(r-1, c) + 
                        dfs(r+1, c) +
                        dfs(r, c-1) + 
                        dfs(r, c+1))
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))
                    # area = dfs(r,c)
        
        #ans = area * 4 - (area - 1) * 2
        ans = 2 * area + 2
        
        return ans
s = Solution()
grid1 = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(s.islandPerimeter(grid1)) # expect 16



# --- End --- #