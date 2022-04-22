# 669. Trim a Binary Search Tree
# Medium


# Larry, https://www.youtube.com/watch?v=HNqG_40m6Tw
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # trim(node) returns the node that is without any out of bounds element
        def trim(node):
            if node is None:
                return None
            
            if node.val < low:
                return trim(node.right)
            elif node.val > high:
                return trim(node.left)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                
                return node
            
        return trim(root)
# 04/15/2022 15:17