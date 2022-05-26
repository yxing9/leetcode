# 329. Longest Increasing Path in a Matrix
# H


# Larry, https://www.youtube.com/watch?v=gudimzlufI0
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R = len(matrix)
        C = len(matrix[0])
        
        # Gives us the longest increasing path starting at x, y
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        has_cache = [[False] * C for _ in range(R)]
        cache = [[None] * C for _ in range(R)]
        
        # Total time complexity:
        #  Total number of inputs * time per input
        # Total space complexity:
        #  Total number of inputs * space per input
        # x -> 0 to R
        # y -> 0 to C
        #  Total number of inputs -> R * C
        # Time per input -> O(1) -> 3 or 4 checks
        # Total time -> O(R * C) * O(1) -> O(R * C)
        # Total space -> O(R * C) * O(1) -> O(R * C)
        def longest(x, y):
            best = 1
            
            if has_cache[x][y]:
                return cache[x][y]
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < R and 0 <= ny < C and matrix[x][y] < matrix[nx][ny]:
                    best = max(best, longest(nx, ny) + 1)
                    
            has_cache[x][y] = True
            cache[x][y] = best
            return best
        
        best = 0
        for x in range(R):
            for y in range(C):
                best = max(longest(x, y), best)
        return best
# 05/19/2022 13:01