# 1305. All Elements in Two Binary Search Trees
# Medium


# My initial solution
# recursion tree traversal + sorting
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
            
        lst1 = inorder(root1)
        lst2 = inorder(root2)
        
        ans = lst1 + lst2
        
        return sorted(ans)
# 01/25/2022 19:20
# time O(N log N), N is number of nodes in the input binary tree
# * O(N) for call stack plus O(N log N) for sorting
# space O(N)
# How to improve?

# ----------------------------------------------------------------------

# My 2nd solution without built-in sorting function
# Improved time complexity from O(N log N) to O(N)
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
            
        lst1 = inorder(root1)
        lst2 = inorder(root2)
        
        def mergeTwoLists(lst1, lst2):
            i = j = 0
            ans = []
            while i < len(lst1) and j < len(lst2):
                if lst1[i] < lst2[j]:
                    ans.append(lst1[i])
                    i += 1
                else:
                    ans.append(lst2[j])
                    j += 1
            while i < len(lst1):
                ans.append(lst1[i])
                i += 1
            while j < len(lst2):
                ans.append(lst2[j])
                j += 1
            return ans
        
        return mergeTwoLists(lst1, lst2)
# 01/25/2022 23:51
# time O(N), N is number of nodes
# space O(N)
# Larry's previous solution is the same as mine, at 31:09

# ----------------------------------------------------------------------

# larry, https://www.youtube.com/watch?v=2QF2cduiyF0
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        INF = 10 ** 10
        fake_root1 = TreeNode(-INF, None, root1)
        fake_root2 = TreeNode(-INF, None, root2)
        
        def getNode(node):
            if node is None:
                return
            
            yield from getNode(node.left)
            yield node
            yield from getNode(node.right)
            
        gen1 = iter(getNode(fake_root1))
        gen2 = iter(getNode(fake_root2))
        
        ans = []
        node1 = next(gen1)
        node2 = next(gen2)
        
        left = False
        try:
            while True:
                if node1.val <= node2.val:
                    ans.append(node1.val)
                    left = True
                    node1 = next(gen1)
                else:
                    ans.append(node2.val)
                    left = False
                    node2 = next(gen2)
        except StopIteration:
            if left:
                ans.append(node2.val)
            else:
                ans.append(node1.val)
        
        for x in gen1:
            ans.append(x.val)
        for x in gen2:
            ans.append(x.val)
        
        return ans[2:]
# 01/26/2022 21:40
# I don't understand this code, 
# What I learned from this code:
# 1. yield
# Larry said this is a funky way but he is learning something new




# --- END --- #