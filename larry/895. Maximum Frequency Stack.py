# 895. Maximum Frequency Stack
# Hard


# Larry, https://www.youtube.com/watch?v=ukP0ADvvg2o
class FreqStack:

    def __init__(self):
        self.heap = []
        self.counter = 0
        self.freq = collections.Counter()

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.counter += 1
        
        heapq.heappush(self.heap, (-self.freq[val], -self.counter, val))

    def pop(self) -> int:
        # count, counter, x
        _, _, x = heapq.heappop(self.heap)
        
        self.freq[x] -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

# 03/19/2022 19:51