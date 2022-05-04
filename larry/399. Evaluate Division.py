# 399. Evaluate Division
# Medium


# Larry, https://www.youtube.com/watch?v=jCN8ItOjQ4o
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Floyd-Warshall's -> this is what we'll be doing
        # a / b, b / c -> a / c
        # a /b -> 1 / (b / a)
        
        keys = {}
        def add_key(x):
            if x not in keys:
                keys[x] = len(keys)
                
        def get_key(x):
            if x not in keys:
                return None
            return keys[x]
        
        for x, y in equations:
            add_key(x)
            add_key(y)
            
        N = len(keys)
        v = [[None] * N for _ in range(N)]
        
        for (x, y), current in zip(equations, values):
            a = get_key(x)
            b = get_key(y)
            v[a][b] = 1.
            v[b][b] = 1.
            v[a][b] = current
            v[b][a] = 1. / current
            
        # O(N^3) -> N ~ 40
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if v[i][j] is None and v[i][k] is not None and v[k][j] is not None:
                        v[i][j] = v[i][k] * v[k][j]
                        
        ans = []
        for x, y in queries:
            a = get_key(x)
            b = get_key(y)
            
            if a is not None and b is not None and v[a][b] is not None:
                ans.append(v[a][b])
            else:
                ans.append(-1.0)
                
        return ans
# 04/30/2022 16:15