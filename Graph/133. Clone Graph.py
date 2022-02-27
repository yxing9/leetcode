# 133. Clone Graph
# Medium
# https://leetcode.com/problems/clone-graph/


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


# Larry, https://www.youtube.com/watch?v=DcL9uvLtOAE
class Solution:
    def cloneGraph(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        
        queue = collections.deque()
        seen = set()
        
        def maybe_enqueue(node):
            if node.val not in seen:
                seen.add(node.val)
                queue.append(node)
                
        dupe = {}
        def getter(node):
            if node.val not in dupe:
                dupe[node.val] = Node(node.val)
            return dupe[node.val]
        
        first = getter(root)
        maybe_enqueue(root)
        while len(queue) > 0:
            current = queue.popleft()
            current_dupe = getter(current)
            
            for neighbor in current.neighbors:
                current_dupe.neighbors.append(getter(neighbor))
                
            for neighbor in current.neighbors:
                maybe_enqueue(neighbor)
                
        return first
# 02/23/2022 17:04







# 7/25/2021
# Pathrise's solution in Graph Preworkshop
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        root = node
        clone = {}
        
        queue = deque([node])
        all_nodes = set([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in all_nodes:
                    queue.append(neighbor)
                    all_nodes.add(neighbor)
                    
        for node in all_nodes:
            clone[node] = Node(node.val)
        
        for node in all_nodes:
            for neighbor in node.neighbors:
                clone[node].neighbors.append(clone[neighbor])
                
        return clone[root]