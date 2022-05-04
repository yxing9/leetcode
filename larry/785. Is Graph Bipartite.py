# 785. Is Graph Bipartite?
# Medium


# Larry, https://www.youtube.com/watch?v=vqtxpWuRrYU
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        BLANK = 0
        WHITE = 1
        BLACK = 2
        
        N = len(graph)
        colors = [BLANK] * N
        
        # is the graph connected at "start" two-colorable
        def two_colorable(start):
            q = collections.deque()
            
            q.append(start)
            colors[start] = WHITE
            
            while len(q) > 0:
                current = q.popleft()
                
                for v in graph[current]:
                    if colors[v] != BLANK and colors[v] == colors[current]:
                        return False
                    
                    if colors[v] == BLANK:
                        if colors[current] == WHITE:
                            colors[v] = BLACK
                        else:
                            colors[v] = WHITE
                        q.append(v)
                        
            return True
        
        for i in range(N):
            if colors[i] == BLANK:
                if not two_colorable(i):
                    return False
                
        # O(V + E) time
        # O(V) space
        return True
# 04/29/2022 16:53