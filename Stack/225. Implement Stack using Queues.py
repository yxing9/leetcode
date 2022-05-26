# 225. Implement Stack using Queues
# E


# Rewrote after Larry, https://www.youtube.com/watch?v=1nBDq83yViI&list=PLP446CXRka0XhT9eav5XUSHbvlnASnzs1&index=22&t=1s
class MyStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        N = len(self.q)
        
        self.q.append(x)
        
        """
        [1]
        append 2 -> [1, 2] -> [2, 1]
        """
        
        for _ in range(N):
            y = self.q.popleft()
            self.q.append(y)

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
# 05/26/2022 16:08



# my one queue solution
class MyStack:

    def __init__(self):
        self.outQueue = collections.deque()

    def push(self, x: int) -> None:
        self.outQueue.append(x)

    def pop(self) -> int:
        return self.outQueue.pop()

    def top(self) -> int:
        return self.outQueue[-1]

    def empty(self) -> bool:
        if not self.outQueue:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# 05/26/2022 15:39