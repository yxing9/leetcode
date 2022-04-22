# 538. Convert BST to Greater Tree
# Medium


# Larry, https://www.youtube.com/watch?v=-HA5Cv7Wg7I
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def convert(node, total):
            if node is None:
                return total
            
            total = convert(node.right, total)
            node.val += total
            total = node.val
            return convert(node.left, total)
        
        convert(root, 0)
        return root
# 04/16/2022 17:13