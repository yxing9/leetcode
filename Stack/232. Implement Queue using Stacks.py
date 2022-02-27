# 232. Implement Queue using Stacks
# Easy


'''

My immediate question is 

Why use 2 stacks only?

Use one stack to record input sequentially and 
the other stack to record in reverse sequence.

----

It's kinda easy if you get it.

Use one stack for input -> achieve push() function
Use another stack for output -> pop() and peek()

If outStack is used up, append everything inStack has to outStack

If both of them are empty, then empty() is empty == the queue if empty

'''

class MyQueue:

    '''
    From clear thoughts to code. I did it!
    '''

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()

    def peek(self) -> int:
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    def empty(self) -> bool:
        if not self.inStack and not self.outStack:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()



# Refactor (Pathrise)
class MyQueue:

    def __init__(self):
        self.inStack, self.outStack = [], []

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        self.move()
        return self.outStack.pop()

    def peek(self) -> int:
        self.move()
        return self.outStack[-1]

    def empty(self) -> bool:
        return (not self.inStack) and (not self.outStack)

    def move(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
# this is faster at 32ms, compared to last one at 47ms