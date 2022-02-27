# 847. Shortest Path Visiting All Nodes
# Hard


# Larry, https://www.youtube.com/watch?v=Ut-keVP8H8E
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        visited = [False, True, False, False, True, True]
                = "FTFFTT"
                = "010011"
                = 010011
                = 19
        """
        N = len(graph)
        
        INF = 10 ** 10
        dist = [[INF] * N for _ in range(N)]
        
        for i, edges in enumerate(graph):
            dist[i][i] = 0
            for edge in edges:
                dist[i][edge] = 1
                
        # Floyd-Warshall's
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
             
        # node -> 1 to 12 -> O(N) = 12
        # visited -> O(2^N) or 2^12
        # possible inputs: O(N * 2^N)
        # each input takes: O(N) time, O(1) space
        # possible total time is O(N^2 * 2^N)
        # possible total space is O(N * 2^N)
        @cache
        def visit(node, visited):
            if visited == (1 << N) - 1:
                return 0
            
            best = INF
            for i in range(N):
                # 1010101111
                # 0000010000
                if ((1 << i) & (visited)) == 0:
                    best = min(best, visit(i, (1 << i) | visited) + dist[node][i])
                    
            return best
        
        best  = INF
        for i in range(N):
            best = min(best, visit(i, (1 << i)))
        return best
# 02/26/2022 15:45