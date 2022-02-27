# 700. Search in a Binary Search Tree
# Easy
# https://leetcode.com/problems/search-in-a-binary-search-tree/


# My first working solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        if root.val < val:
            return self.searchBST(root.right, val)
        if root.val == val:
            return root


# Improved
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        if root.val < val:
            return self.searchBST(root.right, val)
# Time: O(h), with h being the height of the tree. Average case: O(log n). Worst case: O(n).
# Space: O(h), h is tree height. Average case: O(log n). Worst case: O(n).

'''

This tree question is straightforward. 

It's written like a linear question rather than a recursive one.

'''


s = Solution()
print(s.searchBST([4,2,7,1,3], 2)) # expect [2,1,3]
print(s.searchBST([4,2,7,1,3], 5)) # expect []