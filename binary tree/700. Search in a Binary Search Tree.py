# 700. Search in a Binary Search Tree
# Easy
# https://leetcode.com/problems/search-in-a-binary-search-tree/

# ----------------
# 04/14/2022
'''
Now I don't understand how I wrote my solutions in July last year

why this code would not work
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return []
        
        if root.val > val:
            self.searchBST(root.left, val)
        elif root.val < val:
            self.searchBST(root.right, val)
        else:
            return [root.val]
* I don't need [ ] since returning root is already returning a subtree with the node root
'''


# Larry, https://www.youtube.com/watch?v=Ac6BR9yBbSk
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root
        
        while current is not None:
            if current.val == val:
                return current
            elif current.val < val:
                current = current.right
            else:
                current = current.left
        return None
# 04/14/2022 13:50
# O(h) time, h is height of the tree
# O(1) space
# iterative
# for the subtree of the matching node, return current is smart and is enough


# ----------------
# 7/20/2021

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
4/14
It's still solved using recursion.

'''


s = Solution()
print(s.searchBST([4,2,7,1,3], 2)) # expect [2,1,3]
print(s.searchBST([4,2,7,1,3], 5)) # expect []