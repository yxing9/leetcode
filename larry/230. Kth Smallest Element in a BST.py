# 230. Kth Smallest Element in a BST
# Medium


# Larry, https://www.youtube.com/watch?v=w8w_MVvFZ8I
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = None
        left = k
        
        def inorder(node):
            if node is None:
                return
            nonlocal left
            if left < 0:
                return
            
            inorder(node.left)
            left -= 1
            if left == 0:
                nonlocal result
                result = node.val
            inorder(node.right)
        
        inorder(root)
        return result
# 04/18/2022 12:29