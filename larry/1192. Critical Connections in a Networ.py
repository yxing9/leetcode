# 1192. Critical Connections in a Network
# H


# Larry, https://www.youtube.com/watch?v=INqkePQuJoM
class Solution:
    def criticalConnections(self, N: int, connections: List[List[int]]) -> List[List[int]]:
        # bridge finding
        
        edges = collections.defaultdict(list)
        for u, v in connections:
            edges[u].append(v)
            edges[v].append(u)
            
        time = 0
        timeSeen = [None] * N
        earliest = [None] * N
        
        ans = []
        # dfs -> return the earliest node that this has
        def dfs(node, parent):
            nonlocal time
            timeSeen[node] = time
            earliest[node] = time
            time += 1
            
            for v in edges[node]:
                if v != parent:
                    if timeSeen[v] is None:
                        earliestPerNode = dfs(v, node)
                        earliest[node] = min(earliest[node], earliestPerNode)
                        
                        if earliestPerNode > timeSeen[node]:
                            ans.append([node, v])
                    else:
                        earliest[node] = min(earliest[node], earliest[v])
            return earliest[node]
        
        dfs(0, -1)
        return ans
# 05/18/2022 14:00