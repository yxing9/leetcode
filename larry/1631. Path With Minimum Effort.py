# 1631. Path With Minimum Effort
# Medium


# Larry, https://www.youtube.com/watch?v=yYKRmiuFuL8
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R = len(heights)
        C = len(heights[0])
        
        # O(V) -> O(R * C) -> ~ 10,000
        # binary search -> 10^6 -> log 10^6 -> ~20
        
        if R == 1 and C == 1:
            return 0
        
        left = 0
        right = 10 ** 6
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # if we only connect edges that are "target" differences, can we
        # get from top left to bottom right?
        def connected(target):
            q = collections.deque()
            
            seen = [[False] * C for _ in range(R)]
            
            def enqueue(x, y):
                seen[x][y] = True
                q.append((x, y))
                
            enqueue(0, 0)
            while len(q) > 0:
                x, y = q.popleft()
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < R and 0 <= ny < C and not seen[nx][ny] \
                    and abs(heights[nx][ny] - heights[x][y]) <= target:
                        enqueue(nx, ny)
                        
                        if nx == R - 1 and ny == C - 1:
                            return True
                        
            return False
        
        # inclusive
        # both left and right are possible answers
        # O(log U) where U is 10^6
        while left < right:
            # when this is no longer true, it means left == right
            # that means that we have a range of 1 number
            
            mid = (left + right) // 2
            
            # O(N) or O(R * C)
            if connected(mid):
                # mid is a possible answer
                right = mid
            else:
                # mid is NOT a possible answer
                left = mid + 1
                
        return left
# 04/28/2022 19:42