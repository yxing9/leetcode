# 323. Number of Connected Components in an Undirected Graph
# Medium
# Premium
# similar problem: 547. Number of Provinces


'''

from pathrise workshop example questiona and leetcode list of 75 questions

just use this question to practice dfs

a more propert way to solve is Union Find
made specifically for this type of questions



*Converting the nodes and edges to an adjacency list

n = 5
edges = [[0,1],[1,2],[3,4]]

expect below:
graph = [[1], [0,2], [1], [4], [3]]

'''

# Three ways by using a defaultdict(list):
'''
1. 
from collections import defaultdict
n = 5
edges = [[0,1],[1,2],[3,4]]
graph = defaultdict(list)

for i, j in edges:
    graph[i].append(j)
    graph[j].append(i)

print(graph) # defaultdict(<class 'list'>, {0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3]})


2. 
from collections import defaultdict
n = 5
edges = [[0,1],[1,2],[3,4]]
graph = defaultdict(list)

for i in edges:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

print(graph) # defaultdict(<class 'list'>, {0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3]})


3. Pathrise
n = 5
edges = [[0,1],[1,2],[3,4]]

graph = [[] for i in range(n)]

for node1, node2 in edges:
    graph[node1].append(node2)
    graph[node2].append(node1)
print(graph)


*Why this won't work?

n = 5
edges = [[0,1],[1,2],[3,4]]
adjList = [[]] * n

for i in range(len(edges)):
    adjList[edges[i][0]].append(edges[i][1])
    adjList[edges[i][1]].append(edges[i][0])

print(adjList)

'''

# dfs
# based on pathrise workshop video example question template
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(graph, node, visited):
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(graph, neighbor, visited)

        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        count = 0
        visited = [False] * n
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(graph, node, visited)
                count += 1

        return count
# Runtime: 92 ms, faster than 97.10%


# Two wrong solutions I wrote
'''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def dfs(edges, node, visited):
            nonlocal count
            for node in range(len(edges)):
                if not visited[node]:
                    visited[node] = True
                    dfs(edges, edges[node], visited)
                    count += 1
    
        visited = [False] * n
        visited[0] = True
        count = 0
        dfs(edges, edges[0], visited)
        
        return count


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def dfs(edges, node, visited):
            for neighbor in edges[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(edges, neighbor, visited)

        m = len(edges)
        visited = [False] * n
        count = 0
        
        for node in range(m):
            if not visited[node]:
                visited[node] = True
                dfs(edges, node, visited)
                count += 1
        
        return count
'''