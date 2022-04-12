# 543. Diameter of Binary Tree
# Easy
'''
12/15/2021
gave up
jumped to solution quickly

hint from lc solution
deepest left + deepest right = ans

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0
        
        def maxDepthLeft(root):
            if not root:
                return 0
            
            return 1 + maxDepthLeft(root.left)
        
        def maxDepthRight(root):
            if not root:
                return 0
            
            return 1 + maxDepthRight(root.right)
        
        diameter = max(diameter, maxDepthLeft(root) + maxDepthRight(root))

        return diameter

but this is not correct

After solution: 
It's similar to 104. Maximum Depth of Binary Tree 
get the logic straight of both questions


Just to know that 
diameter = max depth of left + max depth of right + 1 (1 as the root level)

I was right about this formula, but wrong about the separated maxDepth functions.
'''


# Yu Zhou's solution
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def depth(root):
            if not root:
                return 0
            
            left = depth(root.left)
            right = depth(root.right)
            self.res = max(self.res, left + right)
            
            return 1 + max(left, right)
        
        depth(root)
        
        return self.res
# 01/05/2022 22:36
# use self. instead of nonlocal
# shorter and clearer variable 



# this is the correct lc solution
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def maxDepth(root):
            nonlocal diameter
            
            if not root:
                return 0
            
            maxDepthLeft = maxDepth(root.left)
            maxDepthRight = maxDepth(root.right)
            diameter = max(diameter, maxDepthLeft + maxDepthRight)
            
            return 1 + max(maxDepthLeft, maxDepthRight)
            
        maxDepth(root)
        
        return diameter
# Runtime: 40 ms, faster than 89.59%
# time O(n)
# space O(n) due to call stack, O(n) if tree is skewed, O(log n) if balanced
# n is #nodes


# TLE
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def maxDepth(root):
            nonlocal diameter
            
            if not root:
                return 0
            
            diameter = max(diameter, maxDepth(root.left) + maxDepth(root.right))
            
            return 1 + max(maxDepth(root.left), maxDepth(root.right))
            
        maxDepth(root)
        
        return diameter
# Why it has to be a variable?
# To reduce the workload of each recursive call?



# --- End --- #