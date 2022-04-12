# 226. Invert Binary Tree
# Easy
# First: 12/18/2021


'''
this is my first line of code for this question:

        root.left.val, root.right.val = root.right.val, root.left.val


'''



#         left = self.invertTree(root.left)
#         right = self.invertTree(root.right)
        
#         left, right = right, left




# DFS, recursive
# trust yourself
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        root.left, root.right = root.right, root.left
        
        return root
# Runtime: 32 ms, faster than 69.08%
# time O(n)
# space O(n)

# refactor


# lc recursive solution
# don't know why it can't pass
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        temp = root.left
        left = root.right
        right = temp
        
        return root


# ---------

# BFS, iterative
# lc solution and https://leetcode.com/problems/invert-binary-tree/discuss/62714/3-4-lines-Python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        queue = [root]
        
        while queue:
            node = queue.pop()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        
        return root
# Runtime: 32 ms, faster than 69.08%
# new knowledge:
#                 queue += node.left, node.right
