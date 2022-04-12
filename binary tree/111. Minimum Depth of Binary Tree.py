# 111. Minimum Depth of Binary Tree
# Easy
# https://leetcode.com/problems/minimum-depth-of-binary-tree/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left or not root.right:
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right)) # this is for the edge case of single branch tree. this is also the code for max depth.
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
# 36.01%
'''
Referred to Leetcode Discuss.


if None in [root.left, root.right]:

Below is buggy:
if None in [root.left or root.right]:

Why?
'''