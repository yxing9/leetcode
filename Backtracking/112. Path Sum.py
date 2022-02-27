# 112. Path Sum
# Easy
# I don't understand the solutions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Backtrack
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        if not root:
            return False

        # at leaf
        def helper(node, soFar):
            if node.left == None and node.right == None:
                return soFar == targetSum # whether soFar is equal to the targetSum

            # for possible options
            for node in [node.left, node.right]:
        
                if node: # is node valid?
        
                    soFar += node.val
                    if helper(node, soFar):
                        return True
                    soFar -= node.val # backtrack
                
            return False
        
        return helper(root, root.val)
# Runtime: 40 ms, faster than 80.75% of Python3 online submissions for Path Sum.
# Memory Usage: 15.9 MB, less than 25.94% of Python3 online submissions for Path Sum.

# 
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        def helper(node, soFar):
            if node.left == None and node.right == None:
                return soFar == targetSum

            return helper(node.left, soFar + node.left.val) or helper(node.right, soFar + node.right.val)
        
        return helper(root, root.val)
'''
AttributeError: 'NoneType' object has no attribute 'val'
    return helper(node.left, soFar + node.left.val) or helper(node.right, soFar + node.right.val)
Line 16 in helper (Solution.py)
    return helper(root, root.val)
Line 18 in hasPathSum (Solution.py)
    ret = Solution().hasPathSum(param_1, param_2)
Line 42 in _driver (Solution.py)
    _driver()
Line 53 in <module> (Solution.py)
'''

#
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root==None:
            return False 
        def helper(run_sum,root):
            # base case
            if root.left == None and root.right == None:            
                run_sum +=root.val
                if run_sum == targetSum:
                    return True
                return False
            
            run_sum +=root.val
            a=False
            b=False
            if root.left!=None: a=helper(run_sum, root.left)
            if root.right!=None: b=helper(run_sum, root.right)
            return  a or b 
        
        return helper(0,root)