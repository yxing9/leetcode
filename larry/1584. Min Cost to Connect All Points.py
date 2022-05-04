# 1584. Min Cost to Connect All Points
# Medium



# Larry, https://www.youtube.com/watch?v=luuo2wRCZhE
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Kruskal's algorithm
        # Union-Find
        # union
        # find
        # union by rank/size/depth
        # path compression
        
        N = len(points)
        parents = list(x for x in range(N))
        
        def ufind(x):
            if parents[x] != x:
                # if x is not the root of itself, find the root
                parents[x] = ufind(parents[x])
            return parents[x]
        
        def uunion(a, b):
            ua = ufind(a)
            ub = ufind(b)
            
            # make all the children of ua point to root of ub
            parents[ua] = ub
            
        # E log E -> Kruskal's
        edges = []
        
        for i in range(N):
            for j in range(i + 1, N):
                edges.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
                
        edges.sort()
        total = 0
        left = N - 1
        for d, u, v in edges:
            if ufind(u) != ufind(v):
                uunion(u, v)
                total += d
                left -= 1
                
            if left == 0:
                break
                
        return total
# 04/26/2022 19:43