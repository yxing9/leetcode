# 200. Number of Islands
# BFS


# refactor 11/24/2021
'''

what if the input grid cannot be overwritten?
i tried a hash set visited but failed, why?

'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(matrix, r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] != "1":
                return
            matrix[r][c] = "#"
            dfs(matrix, r-1, c)
            dfs(matrix, r+1, c)
            dfs(matrix, r, c-1)
            dfs(matrix, r, c+1)

        rows, cols = len(grid), len(grid[0])
        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(grid, r, c)
                    ans += 1
        
        return ans
# Runtime: 471 ms, faster than 14.26%



# my refactor after previous tries
# 11/23/2021
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(matrix, row, col):
            if row < 0 or row > len(matrix)-1 or col < 0 or col > len(matrix[0])-1 or matrix[row][col] != '1':
                return
            matrix[row][col] = '#'
            dfs(matrix, row-1, col)
            dfs(matrix, row+1, col)
            dfs(matrix, row, col-1)
            dfs(matrix, row, col+1)

        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    num += 1
        
        return num
# Runtime: 580 ms, faster than 5.51%



# pathrise version
# 11/23
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(grid, row, col):
            if row in range(len(grid)) and col in range(len(grid[row])) and grid[row][col] == "1":
                grid[row][col] = None
                dfs(grid, row-1, col)
                dfs(grid, row+1, col)
                dfs(grid, row, col-1)
                dfs(grid, row, col+1)

        num = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] != None and grid[row][col] == "1":
                    dfs(grid, row, col)
                    num += 1
        
        return num
# Runtime: 400 ms, faster than 25.95% 
# time: O(m * n) m == grid.length    n== grid[i].length
# space: O(1) ? 



# refactor on pathrise version
# 11/23
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != None and grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    num += 1
        return num
    
    def dfs(self, grid, row, col):
        if row in range(len(grid)) and col in range(len(grid[row])) and grid[row][col] == "1":
            grid[row][col] = None
            self.dfs(grid, row-1, col)
            self.dfs(grid, row+1, col)
            self.dfs(grid, row, col-1)
            self.dfs(grid, row, col+1)
# Runtime: 382 ms, faster than 30.04%





# ------------------------------------
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         '''
        
#         grid = [
#                   ["1","1","1","1","0"], i
#                     j   
#                   ["1","1","0","1","0"],
#                   ["1","1","0","0","0"],
#                   ["0","0","0","0","0"]
#                 ]
        
#         for i in range(m):
#             for j in range(n)
        
        
#         grid[i][j]
#         grid[i+1][j]    down
#         grid[i][j+1]    right
        
#         '''