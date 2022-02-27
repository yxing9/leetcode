# 94. Binary Tree Inorder Traversal
# Easy


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# recursion
# learned from daniel kim's youtube
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
# Runtime: 32 ms, faster than 65.87%



# recursive
# 12/01/2021
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        
        def helper(root, res):
            # if root:
            #     helper(root.left, res)
            #     res.append(root.val)
            #     helper(root.right, res)
            if not root:
                return
            helper(root.left, res)
            res.append(root.val)
            helper(root.right, res)
        
    
        helper(root, res)
        return res
# Runtime: 32 ms, faster than 66.33%
# time O(n) n is number of node
# space O(n)
# I didn't know how to 
# 1. root.left
# 2. root.val



# iterative
# 12/01/2021
# lc solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = []
        res = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        
        return res
# Runtime: 32 ms, faster than 65.87%
# time O(n)
# space O(n)
# I don't understand this solution