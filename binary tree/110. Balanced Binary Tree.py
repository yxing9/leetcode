# 110. Balanced Binary Tree
# Easy
# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        left = self.maxHeight(root.left)
        right = self.maxHeight(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def maxHeight(self, root):
        if not root:
            return 0
        left = self.maxHeight(root.left)
        right = self.maxHeight(root.right)
        return max(left, right) + 1
# 5.36%
# Time O(n log n)
# Space O(height)
'''
Q3 in Binary Tree workshop
I dont fully understand
'''