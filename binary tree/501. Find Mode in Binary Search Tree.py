# 501. Find Mode in Binary Search Tree
# Easy
# https://leetcode.com/problems/find-mode-in-binary-search-tree/
# 1st example problem in Binary Tree Workshop

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    max_count = 0
    cur_count = 0
    res = []

    def findMode(self, root: TreeNode) -> List[int]:
        self.inOrderDFS(root)
        return self.res

    def inOrderDFS(self, node):
        if not node:
            return 
        self.inOrderDFS(node.left)

        self.cur_count = 1 if self.prev != node.val else self.cur_count + 1

        if self.cur_count == self.max_count:
            self.res.append(node.val)
            
        elif self.cur_count > self.max_count:
            self.max_count = self.cur_count
            self.res = [node.val]
            
        self.prev = node.val
        self.inOrderDFS(node.right)
# Time O(b^h) to traverse all nodes
'''
Based on Pathrise's DFS template, revised using the following code from Leetcode Discuss:

class Solution(object):
    prev = None
    max_count = 0
    current_count = 0 
    result = []

    def findMode(self, root):
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if not node: return
        self.dfs(node.left)
        self.current_count = 1 if node.val != self.prev else self.current_count + 1
        if self.current_count == self.max_count:
            self.result.append(node.val)
        elif self.current_count > self.max_count:
            self.result = [node.val]
            self.max_count = self.current_count
        self.prev = node.val
        self.dfs(node.right)
'''