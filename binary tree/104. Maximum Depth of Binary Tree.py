# 104. Maximum Depth of Binary Tree
# Easy
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        else:
            return 0
# Time O(2^n)
# 6.43%
'''
1st question in pathrise Binary Tree pre-workshop

Inspired by pathrise pre-workshop and corrected by leetcode discuss.

Recursion with O(2^n) time. No surprise it's slow.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1
# 8.61%
'''
Re-appeared as Q2 in Binary Search Workshop

Solved using Pathrise's binary tree height template
'''