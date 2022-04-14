# 59. Spiral Matrix II
# Medium


# Larry, https://www.youtube.com/watch?v=5tGQ6VsPHgg&t=8s
class Solution:
    def generateMatrix(self, N: int) -> List[List[int]]:
        matrix = [[None] * N for _ in range(N)]
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        current_direction = 0
        
        for a in range(1, N * N + 1):
            matrix[x][y] = a
            
            if a == N * N:
                continue
                
            while True:
                dx, dy = directions[current_direction]
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] is None:
                    x, y = nx, ny
                    break
                    
                current_direction += 1
                current_direction %= 4
                
        return matrix
# 04/13/2022 17:51