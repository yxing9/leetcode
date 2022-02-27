# 701. Insert into a Binary Search Tree
# Medium


'''
My thought process:

naive approach
1. see where can this node be inserted into

       4
     /   \
    2     7
   / \   e f
  1   3
 a b c d

No, I don't think this naive approach would work, 
because the new node can also be inserted as the root node. 

all possible places we can insert the new node into are:
(num of leaf nodes * 2) / 2 + num of total nodes - num of leaf nodes = num of total nodes

2. always think about the sorted nature when it comes to BST
1) get the list via inorder traversal
1,2,3,4,7    val = 5
we can easily see that there's only 2 places we can insert the new node into, the places are 
    - either we put it after 4, but since 4 is not a leaf node, we replace 4 with 5 instead
    - or we put it before 7, since 7 is indeed a leaf node, it becomes easy, we just insert it into root.left of 7


Is this a step we must take?
run a inorder traversal to check if the array is sorted

how to insert a new node, I think it is just 
if val < root.val:
    root.left = val
else:
    root.right = val


? What is the node I want to replace is not a leaf node?


Give up here to look at Larry's solution.

----------

Larry's explanation
https://www.youtube.com/watch?v=ok5Fuq0KJZE

why i didn't think about checking each root.val with val if smaller go left, big go right?
it's pretty straight forward, isn't it?


'''



# Larry's explanation and code, I changed a little
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        current = root
        
        while current: # or while True
            if val < current.val:
                if current.left is None:
                    current.left = TreeNode(val)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(val)
                    break
                else:
                    current = current.right
                
        return root
# 01/12/2022 01:12
# time O(H), H is the height of the tree
# space O(1)
'''
Larry did this in the beginning

INF = 10 ** 10
newRoot = TreeNode(-INF)
newRoot.right = root
current = newRoot

instead of just

if not root:
    return TreeNode(val)


'''



# ----------

# my initial wrong try
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        nums = inorder(root)
        
        def binarySearch(nums, target):
            l, r = 0, len(nums)-1
            while l < r:
                m = l + (r - l) // 2
                if m > target:
                    r = m
                if m < target:
                    l = m
            return l



# --- End --- #