# 138. Copy List with Random Pointer
# Medium


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# Larry, https://www.youtube.com/watch?v=_0tFJ5lp79c
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newHead = Node(-1)
        newHead.next = head
        
        current = newHead
        
        ansHead = Node(-1)
        ansCurrent = ansHead
        
        # deepcopy without the random edge
        def dc(node):
            if node is None:
                return None
            return Node(node.val)
        
        while current is not None:
            ansCurrent.next = dc(current.next)
            ansCurrent = ansCurrent.next
            current = current.next
            
        lookup = {}
        current = newHead
        ansCurrent = ansHead
        
        while current is not None:
            lookup[current] = ansCurrent
            
            ansCurrent = ansCurrent.next
            current = current.next
            
        current = newHead
        ansCurrent = ansHead
        
        while current is not None:
            if current.random is not None:
                ansCurrent.random = lookup[current.random]
            else:
                ansCurrent.random = None
                
            ansCurrent = ansCurrent.next
            current = current.next
            
        return ansHead.next
# 03/12/2022 18:22