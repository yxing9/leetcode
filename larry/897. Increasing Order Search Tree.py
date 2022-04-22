# 897. Increasing Order Search Tree
# Easy


# my initial solution
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        inorderList = []
        def inorder(root):
            nonlocal inorderList
            if root:
                inorder(root.left)
                inorderList.append(root.val)
                inorder(root.right)
        
        inorder(root)
        
        def constructTree(listOfNodes):
            # for _ in listOfNodes:


# Larry, https://www.youtube.com/watch?v=Hb8OCZUajyY
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        sentinel = TreeNode(-1)
        tail = sentinel
        
        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)
            nonlocal tail
            tail.right = node
            tail.left = None
            tail = tail.right
            tail.left = None
            inorder(node.right)
            tail.right = None
            
        inorder(root)
        return sentinel.right
# 04/17/2022 15:31