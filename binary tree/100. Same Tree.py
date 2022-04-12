# 100. Same Tree
# Easy
# https://leetcode.com/problems/same-tree/

'''
2nd question in pathrise Binary Tree pre-workshop

if TreeNode.p.root == TreeNode.q.root and TreeNode.p.root.left ==TreeNode.q.left and TreeNode.p.root.right == TreeNode.q.root.right:
    return True
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# 59.16%
# Referred to Leetcode solution, Recursion
# Easy to think of when I wrote the 2nd and 3rd conditions before the 1st one