# 99. Recover Binary Search Tree
# Medium


# Larry, https://www.youtube.com/watch?v=gK-6V_joIro
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        """
           13
          / \
        10   20
        /\   / \
       1 15 12 25
            /\
           14 16 
        """
        previousNode = None
        arr = []
        
        # Add Morris Traversal
        # linear time, linear space
        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)
            
            nonlocal previousNode
            if previousNode is not None and previousNode.val > node.val:
                if len(arr) == 0:
                    arr.append(previousNode)
                if len(arr) < 2:
                    arr.append(node)
                else:
                    arr[1] = node
            previousNode = node
            inorder(node.right)
            
        inorder(root)
        
        assert(len(arr) == 2)
        arr[0].val, arr[1].val = arr[1].val, arr[0].val
# 04/19/2022 17:41



'''

exactly two nodes


inorder traversal in BST == sorted array

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []



----

LC solution

approach 1:
1. construct inorder traversal (to get an almost sorted array)
2. locate which two nodes are swapped 
3. swap the value of the two nodes


1. 
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []

2. 
def findSwapped(nums):
    n = len(nums)
    x = y = -1
    for i in range(n-1):
        if nums[i+1] < nums[i]:
            y = nums[i+1]
            if x == -1:
                x = nums[i]
    return x, y
    
print(findSwapped([3,2,1]))

3. 
x, y = y, x



'''


# Timothy Chang's sorting solution
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        
        Timothy Chang's solution, https://www.youtube.com/watch?v=bJBwOMPhe6Y
        """
        self.temp = []
        
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.temp.append(root)
            dfs(root.right)
        
        dfs(root)
        
        srt = sorted(n.val for n in self.temp)
        
        for i in range(len(srt)):
            self.temp[i].val = srt[i]
# 01/05/2022 21:52
# time O(n log n), sorting
# space O(n), call stack



# -----

# this lc solution doesn't work for the case of [-1,null,-3,null,-2,null,-4]
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        
        def findSwapped(nums):
            n = len(nums)
            x = y = -1
            for i in range(n-1):
                if nums[i+1] < nums[i]:
                    y = nums[i+1]
                    if x == -1:
                        x = nums[i]
            return x, y
        
        def recover(root, count):
            if root:
                if root.val == x or root.val == y:
                    if root.val == x:
                        root.val = y
                    elif root.val == y:
                        root.val = x
                    count -= 1
                    if count == 0:
                        return
                recover(root.left, count)
                recover(root.right, count)
            
        nums = inorder(root)
        x, y = findSwapped(nums)
        recover(root, 2)



# ------


# I should try 
# iterative inorder solution in O(n) time and O(n) space
# recursive inorder solution in O(n) time and O(n) space
# Morris inorder in O(n) time and O(1) space 

# but I haven't 





# --- End --- #