# 1260. Shift 2D Grid
# Easy



# Larry, https://www.youtube.com/watch?v=CYx-Xddv-mc
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        R = len(grid)
        C = len(grid[0])
        
        matrix = [[None] * C for _ in range(R)]
        
        def shift(x, y, k):
            position = (x * C + y + k) % (R * C)
            
            return (position // C, position % C)
        
        for i in range(R):
            for j in range(C):
                pi, pj = shift(i, j, k)
                matrix[pi][pj] = grid[i][j]
        return matrix
# 04/29/2022 16:46