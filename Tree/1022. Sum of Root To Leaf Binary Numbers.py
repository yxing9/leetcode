# 1022. Sum of Root To Leaf Binary Numbers
# Easy


'''

3 ways to do DFS 
1. Iterative
2. Recursive
    - simplest to write
3. Morris
    - O(1) space

------

Review 

Recursive DFS preorder, postorder, and inorder:
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/solution/

def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []

def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] + if root else []

def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) + if root else []

*but I like to name them all dfs()

#preorder
def dfs(root):
    return [root.val] + dfs(root.left) + dfs(root.right) + if root else []

# postorder
def dfs(root):
    return dfs(root.left) + dfs(root.right) + [root.val] + if root else []

# inorder
def dfs(root):
    return dfs(root.left) + [root.val] + dfs(root.right) + if root else []


------

Learned from Larry:

shift and add method 

for binary multiplication

'''




# lc solution recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        '''
        lc recursive solution
        '''
        def preorder(root, curr_number):
            nonlocal root_to_leaf
            
            if root:
                curr_number = (curr_number << 1) | root.val
                if not (root.left or root.right):
                    root_to_leaf += curr_number
                preorder(root.left, curr_number)
                preorder(root.right, curr_number)
        
        root_to_leaf = 0
        preorder(root, 0)
        
        return root_to_leaf
# 01/10/2022 23:57
# i am confused



# ---- 

# my try
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        node = []
        res = []
        
        def dfs(root):
            nonlocal node
            
            
            if not root:
                res.append(node)
                node = []
                return
            
            node.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        
        print(node)
        print(res)
# not sure how to fix it



# ---- 

# larry's solution
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        '''
        larry's, https://www.youtube.com/watch?v=RbfgwEs2cSM
        '''
        def total(root, current):
            if not root:
                return 0
                
            current = current * 2 + root.val
            
            if not root.left and not root.right:
                return current
                
            return total(root.left, current) + total(root.right, current)
        
        return total(root, 0)
# 01/11/2022 01:55
# time O(n)
# space O(n) for call stack
# Could you explain more why current = current * 2 + root.val? 
# I don't understand how it adds up those binary values and converts it to decimal. 
# You said in the video "shifting the digit one over and adding the next number to it" but I am still confused. Thanks!
# shift and add 


# --- End --- #