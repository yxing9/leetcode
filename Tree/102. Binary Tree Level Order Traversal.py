# 102. Binary Tree Level Order Traversal
# Medium
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        res = []
        
        while queue:
            cur_level = []
            size = len(queue)
            
            for _ in range(size):
                node = queue.popleft()
                cur_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cur_level)
            
        return res
# 5.55%
'''
Fully copied Pathrise's BFS MIKE template
make a queue
iterate over the queue
keep track of the size of the queue
expand the child nodes

I dont fully understand this question.
'''