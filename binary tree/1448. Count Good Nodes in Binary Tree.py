# 1448. Count Good Nodes in Binary Tree
# Medium


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    
    pathrise pair programming solution
    
    '''
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_val):
            nonlocal count
            if not node:
                return

            if node.val >= max_val:
                count += 1
                max_val = node.val

            dfs(node.left, max_val)
            dfs(node.right, max_val)

        count = 0
        dfs(root, -math.inf)
        return count
# Runtime: 432 ms, faster than 5.01%

# ------

# Hanlin Ye's solution
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def preorder(curr, val):
            if not curr:
                return 0
            updateMax = max(val, curr.val)
            if curr.val >= val:
                return 1 + preorder(curr.left, updateMax) + preorder(curr.right, updateMax)
            else:
                return preorder(curr.left, updateMax) + preorder(curr.right, updateMax)
        return preorder(root, root.val)
# Runtime: 252 ms, faster than 62.39%

# ------

from collections import deque
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        pathrise pair programming's wrong answer
        let me debug if time
        '''
        count = 0
        stack_nodes = deque([])
    
        def dfs(root):
            nonlocal count
            flag = True
            stack_nodes.append(root.val)
            if stack_nodes:
                for i in range(len(stack_nodes)):
                    if(stack_nodes[i] > root.val):
                        flag = False
                if flag == True:
                    count+=1
            
            # leaf
            if(root.left and root.right):
                stack_nodes.popleft()
                return
            #root
            # stack_nodes.append(root.val)
            if( root.left):
                dfs(root.left)
            # stack_nodes.popleft()
            if(root.right):
                dfs(root.right)

            stack_nodes.popleft()
  
        if root:  
            dfs(root)
        return count