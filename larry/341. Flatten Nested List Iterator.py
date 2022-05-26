# 341. Flatten Nested List Iterator
# Medium



# Larry, https://www.youtube.com/watch?v=MNdAkibFWXE
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = nestedList
        
        self.stack = []
        if len(self.list) > 0:
            self.stack.append((self.list, 0))
        self.__adjustNext()
    
    def __adjustNext(self) -> int:
        # Make sure that top of the stack contains an integer
        if len(self.stack) == 0:
            return
        
        while len(self.stack) > 0:
            nestedList, index = self.stack[-1]
            if nestedList[index].isInteger():
                return
            
            nextLevel = nestedList[index].getList()
            if len(nextLevel) > 0:
                self.stack.append((nextLevel, 0))
            else:
                self.__movePointer()
                
    def __movePointer(self):
        while len(self.stack) > 0:
            nestedList, index = self.stack[-1]
            
            if index + 1 < len(nestedList):
                self.stack.pop()
                self.stack.append((nestedList, index + 1))
                return
            else:
                self.stack.pop()
                
    def __increment(self):
        self.__movePointer()
        self.__adjustNext()
        
    def next(self) -> int:
        assert(len(self.stack) > 0)
        
        nestedList, index = self.stack[-1]
        result = nestedList[index]
        self.__increment()
        return result
    
    def hasNext(self) -> bool:
         return len(self.stack) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# 05/08/2022 17:49