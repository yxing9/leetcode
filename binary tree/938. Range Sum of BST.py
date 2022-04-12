# 938. Range Sum of BST
# Easy
# Binary Tree


# my brute force solution
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        
        def helper(root):
            nonlocal ans
            
            if not root:
                return
            
            if root.val in range(low, high+1):
                ans += root.val
            
            helper(root.left)
            helper(root.right)
        
        helper(root)
        
        return ans
# Runtime: 284 ms, faster than 20.59%
# time O(n)
# space O(n) for recursive stack



# 2nd time doing this problem, saw my last time's solution on lc then write up
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.result = 0
        
        def dfs(root, low, high):
            if not root:
                return 0
            
            if low <= root.val <= high:
                self.result += root.val
                
            dfs(root.left, low, high)
            dfs(root.right, low, high)
            
        dfs(root, low, high)
        
        return self.result
# 01/18/2022 22:36



# --- END --- #