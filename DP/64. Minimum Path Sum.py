# 64. Minimum Path Sum
# Medium



# DP Memorization
class Solution:
    def minPathSum(self, grid):
        
        # Set a separate dict to avoid recursive calls
        return self.minPathSumDriver(grid, 0, 0, {})
    
    def minPathSumDriver(self, grid, r, c, memo) -> int:    
        
        # Base case: when row or column goes out of bound
        if r == len(grid) or c == len(grid[0]):
            return float('inf')
        
        # Memoization
        key = (r, c)
        if key in memo:
            return memo[key]
        
        # Exiting condition: when the target is reached
        if r == len(grid)-1 and c == len(grid[0])-1:
            return grid[r][c]
        
        right = self.minPathSumDriver(grid, r, c+1, memo)
        down = self.minPathSumDriver(grid, r+1, c, memo)
        
        memo[key] = grid[r][c] + min(right, down)
        return memo[key]
# time: O(m * n) m is number of rows and n is number of columns
# space: 
'''

    def minPathSum(self, grid):
        
        # Set a separate dict to avoid recursive calls
        memo = {}
        return self.minPathSumDriver(grid, 0, 0, memo)

'''
# Buggy code of DP memo
class Solution:
    def minPathSum(self, grid, r=0, c=0, memo={}) -> int:
        
        # Base case: when row or column goes out of bound
        if r == len(grid) or c == len(grid[0]):
            return float('inf')
        
        # Memorization
        key = (r, c)
        if key in memo:
            return memo[key]
        
        # Exiting condition: when the target is reached
        if r == len(grid)-1 and c == len(grid[0])-1:
            return grid[r][c]
        
        right = self.minPathSum(grid, r, c+1, memo)
        down = self.minPathSum(grid, r+1, c, memo)
        
        memo[key] = grid[r][c] + min(right, down)
        return memo[key]
# This code has a bug of repeating the result from the first input



# # Without memorization -> TLE
# class Solution:
#     def minPathSum(self, grid: List[List[int]], r=0, c=0) -> int:
        
#         # Base case: when row or column goes out of bound
#         if r == len(grid) or c == len(grid[0]):
#             return float('inf')
        
#         # Exiting condition: when the target is reached
#         if r == len(grid)-1 and c == len(grid[0])-1:
#             return grid[r][c]
        
#         right = self.minPathSum(grid, r, c+1)
#         down = self.minPathSum(grid, r+1, c)
        
#         # Add current number to the mininum number to minimize path sum
#         return grid[r][c] + min(right, down)

# A tip:
# Avoid being clear on your code
# You would want to use 
#         return grid[r][c] + min(self.minPathSum(grid, r, c+1), self.minPathSum(grid, r+1, c))
# instead of 
#         right = self.minPathSum(grid, r, c+1)
#         down = self.minPathSum(grid, r+1, c)
        
#         # Add current number to the mininum number to minimize path sum
#         return grid[r][c] + min(right, down)



s = Solution()
print(s.minPathSum([[1,2,3],[4,5,6]])) # expect 12
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]])) # expect 7