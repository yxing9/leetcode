# 1091. Shortest Path in Binary Matrix
# M


# Larry, https://www.youtube.com/watch?v=J_o6XVRXuHs
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        
        q = collections.deque()
        
        INF = 10 ** 15
        dist = [[INF] * C for _ in range(R)]
        
        def enqueue(x, y, d):
            dist[x][y] = d
            q.append((x, y, d))
            
        if grid[0][0] == 0:
            enqueue(0, 0, 1)
            
        directions = [(1, 0), (1, -1), (1, 1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]
        
        while len(q) > 0:
            x, y, d = q.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 0 and dist[nx][ny] == INF:
                    enqueue(nx, ny, d + 1)
                    
        if dist[R - 1][C - 1] == INF:
            return -1
        return dist[R - 1][C - 1]
# 05/16/2022 18:27