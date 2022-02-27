# 547. Number of Provinces
# Medium
# 323. Number of Connected Components in an Undirected Graph


isConnected = [[1,1,0],[1,1,0],[0,0,1]]


'''

                  [[1,1,0],[1,1,0],[0,0,1]]
isConnected[i]      0         1         2
isConnected[i][j]   0 1 2

rule out 0
rule out itself

if isConnected[i][j] != 0 and isConnected[i][j] != isConnected[i][i]


'''

# my dfs solution
from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(graph, node, visited):
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(graph, neighbor, visited)
        
        graph = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] != 0 and j != i:
                    graph[i].append(j)
                    
        visited = [False] * n
        count = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(graph, node, visited)
                count += 1
        
        return count
# Runtime: 188 ms, faster than 80.21%

'''

from collections import defaultdict

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
n = len(isConnected)
# graph = [[]] * n
graph = defaultdict(list)

for i in range(n):
  for j in range(n):
    if isConnected[i][j] != 0 and i != j:
      # graph[i] = [j]
        graph[i].append(j)
print(graph)
print(graph[2])

'''