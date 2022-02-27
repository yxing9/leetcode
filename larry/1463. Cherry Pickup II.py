# 1463. Cherry Pickup II
# Hard
# DP


'''

2 robots!!

(i + 1, j - 1)       (i + 1, j)        (i + 1, j + 1)
to the down left     vertical down     to the down right

=> no lateral movement => only one cell at one row




'''


# Larry's
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        '''
        Larry's, https://www.youtube.com/watch?v=3xUoMISRD3s
        '''
        R = len(grid)
        C = len(grid[0])
        
        calculated = [[[False] * (C + 1) for _ in range(C+1)] for _ in range(R + 1)]
        cache = [[[None] * (C + 1) for _ in range(C + 1)] for _ in range(R + 1)]
        
        # row -> 0 to rows -> O(R)
        # c1 -> 0 to cols -> O(C)
        # c2 -> 0 to cols -> O(C)
        # number of total possible inputs = O(R * C^2)
        # work each input does is O(1)
        # total complexity is O(R * C^2)
        
        def maxCherry(row, c1, c2):
            if row == R:
                return 0
            if calculated[row][c1][c2]:
                return cache[row][c1][c2]
            
            best = 0
            for dc1 in [-1, 0, 1]:
                for dc2 in [-1, 0, 1]:
                    nc1, nc2 = c1 + dc1, c2 + dc2
                    
                    if 0 <= nc1 < C and 0 <= nc2 < C:
                        cherry = grid[row][c1]
                        if c1 != c2:
                            cherry += grid[row][c2]
                        best = max(best, maxCherry(row + 1, nc1, nc2) + cherry)
                        
            calculated[row][c1][c2] = True
            cache[row][c1][c2] = best
            
            return best
        
        return maxCherry(0, 0, C - 1)
# https://www.youtube.com/watch?v=HKxM2ztnMhA
# https://www.youtube.com/watch?v=3xUoMISRD3s