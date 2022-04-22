# 173. Binary Search Tree Iterator
# Medium


# Larry, https://www.youtube.com/watch?v=szi2xljWkN8
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.__process_left(root)

    def __process_left(self, node):
        current = node
        
        while current is not None:
            self.stack.append(current)
            current = current.left
            
    def next(self) -> int:
        node = self.stack[-1]
        rval = node.val
        
        self.stack.pop()
        if node.right is not None:
            self.__process_left(node.right)
            
        return rval

    def hasNext(self) -> bool:
        return len(self.stack) > 0
# 04/20/2022 19:55