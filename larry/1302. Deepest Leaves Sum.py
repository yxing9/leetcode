# 1302. Deepest Leaves Sum
# M



# Larry, https://www.youtube.com/watch?v=VNMRR76AwAU
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deepest = -1
        total = 0
        
        def recurse(node, depth):
            if node is None:
                return
            
            if node.left is None and node.right is None:
                nonlocal deepest
                nonlocal total
                if deepest < depth:
                    deepest = depth
                    total = 0
                    
                if deepest == depth:
                    total += node.val
            else:
                recurse(node.left, depth + 1)
                recurse(node.right, depth + 1)
                
        recurse(root, 0)
        return total
# 05/15/2022 17:13