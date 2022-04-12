# 1046. Last Stone Weight
# Easy


# Larry, https://www.youtube.com/watch?v=onLtIoKhcFs
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        
        def push(x):
            heapq.heappush(h, -x)
            
        def pop():
            return -heapq.heappop(h)
        
        for x in stones:
            push(x)
            
        # O(N) iterations
        while len(h) > 1:
            # O(log N)
            x = pop()
            y = pop()
            
            if x != y:
                push(abs(x - y))
            
        if len(h) == 0:
            return 0
        return pop()
# 04/07/2022 12:06