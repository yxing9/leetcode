# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
# M


# Larry, https://www.youtube.com/watch?v=K4BjZxxYMlI
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def traverse(nodeOriginal, nodeCloned, target):
            if nodeOriginal is None:
                return None
            
            if nodeOriginal == target:
                return nodeCloned
            
            return traverse(nodeOriginal.left, nodeCloned.left, target) or traverse(nodeOriginal.right, nodeCloned.right, target)
        
        return traverse(original, cloned, target)
# 05/17/2022 18:47