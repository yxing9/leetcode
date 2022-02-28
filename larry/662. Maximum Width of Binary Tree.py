# 662. Maximum Width of Binary Tree
# Medium


# Larry, https://www.youtube.com/watch?v=Enp3m3F8FSg
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #INF = 10 ** 10
        INF = float('inf')
        
        leftmost = collections.defaultdict(lambda: INF)
        rightmost = collections.defaultdict(lambda: -INF)
        
        def go(node, level, num):
            if node is None:
                return
            
            leftmost[level] = min(leftmost[level], num)
            rightmost[level] = max(rightmost[level], num)
            
            go(node.left, level + 1, num * 2 + 1)
            go(node.right, level + 1, num * 2 + 2)
            
        go(root, 0, 1)
        
        best = 1
        for level in leftmost.keys():
            best = max(best, rightmost[level] - leftmost[level] + 1)
        return best