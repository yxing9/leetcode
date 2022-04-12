# 257. Binary Tree Paths
# Easy


# pathrise leetcode solution
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def helper(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path) # at leaf node, now path is complete, push to paths
                else:
                    path += '->'
                    helper(root.left, path)
                    helper(root.right,path)
        
        paths = []
        helper(root, '')
        
        return paths
# time O(n)
# space O(n)


# my initial writeup
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        '''
        input  [1,2,3,null,5]
        output [1,2,5,3]
        expect ["1->2->5","1->3"]
        '''
        
        res = []
        
        def helper(root):
            if not root:
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        
        helper(root)
        
        return res