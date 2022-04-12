# 563. Binary Tree Tilt
# Easy


'''
below was my initial try
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        sum_tilt = 0
        
        def helper(root):                                         # add nonlocal sum_tilt
            if not root:
                tilt = 0                                          # this is recursion. return 0
        
            tilt = abs(helper(root.left) - helper(root.right))    # use seperate variables for left and right
            sum_tile += tilt                                      # typo
                                                                  # missing one key line. return root.val + left_sum + right_sum
        helper(root)
        
        return sum_tilt
'''


# failed at [4,2,9,3,5,null,7]
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        sum_tilt = 0
        
        def tiltSum(root):
            nonlocal sum_tilt
            
            if not root:
                return 0
            
            tilt = abs(tiltSum(root.left) - tiltSum(root.right))
            sum_tilt += tilt
            
            return root.val + tiltSum(root.left) + tiltSum(root.right)
        
        tiltSum(root)
        
        return sum_tilt
# I guess I can't put two recursion function in an operation and let them compute


# finally an accpeted solution
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        sum_tilt = 0
        
        def tiltSum(root):
            nonlocal sum_tilt
            
            if not root:
                return 0
            
            left_tilt = tiltSum(root.left)
            right_tilt = tiltSum(root.right)
            tilt = abs(left_tilt - right_tilt)
            sum_tilt += tilt
            
            return root.val + left_tilt + right_tilt
        
        tiltSum(root)
        
        return sum_tilt
# Runtime: 127 ms, faster than 11.86%
# time O(n)
# space O(n) recursion call stack
# postorder traversal, left -> right -> root