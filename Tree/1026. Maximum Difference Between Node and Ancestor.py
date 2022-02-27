# 1026. Maximum Difference Between Node and Ancestor
# Medium


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        cur_min = cur_max = root.val
            
        def helper(root):
            nonlocal cur_min
            nonlocal cur_max
            
            if root:
                cur_min = min(cur_min, root.val)
                cur_max = max(cur_max, root.val)
        
        helper(root.left)
        helper(root.right)
        
        return abs(cur_min - cur_max)


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        cur_min = cur_max = root.val
            
        def helper(root):
            nonlocal cur_min
            nonlocal cur_max
            
            if root:
                cur_min = min(cur_min, root.val)
                cur_max = max(cur_max, root.val)
        
            return abs(cur_min - cur_max)
            
        left = helper(root.left)
        right = helper(root.right)
        
        return max(left, right)


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        cur_min = cur_max = root.val
            
        def helper(root):
            nonlocal cur_min
            nonlocal cur_max
            
            if root:
                cur_min = min(cur_min, root.val)
                cur_max = max(cur_max, root.val)
            
                left = helper(root.left)
                right = helper(root.right)
                
                return max(left, right)
            else:
                return abs(cur_min - cur_max)
        
        return helper(root)


# lc solution
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
            
        def helper(root, cur_min, cur_max):
            if not root:
                return (cur_max - cur_min)
                
            cur_min = min(cur_min, root.val)
            cur_max = max(cur_max, root.val)
            
            left = helper(root.left, cur_min, cur_max)
            right = helper(root.right, cur_min, cur_max)
                
            return max(left, right)
            
        return helper(root, root.val, root.val)
# 12/31/2021 15:51
# time O(n) for recursion call stack 

'''

First three attempts are my thought progress. 

In order to achieve the ancestor part, 
what i did wrong was I can't use one set of max and min and 
use it across all left and right nodes.



'''