# 743. Network Delay Time
# M


# Larry, https://www.youtube.com/watch?v=9rC0xxAChno
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        edges = collections.defaultdict(list)
        
        for u, v, t in times:
            edges[u].append((v, t))
            
        h = []
        
        dist = {}
        
        def push(t, node):
            heapq.heappush(h, (t, node))
            dist[node] = t
            
        push(0, K)
        
        while len(h) > 0:
            t, node = heapq.heappop(h)
            
            if dist[node] < t:
                continue
                
            for v, vt in edges[node]:
                if v not in dist or dist[node] + vt < dist[v]:
                    push(dist[node] + vt, v)
                    
        if len(dist) != N:
            return -1
        
        # O(V + E log E) time -> O(V + E log V)
        # space O(V + E)
        return max(dist.values())
# 05/14/2022 17:01