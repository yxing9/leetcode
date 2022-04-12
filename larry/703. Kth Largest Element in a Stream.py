# 703. Kth Largest Element in a Stream
# Easy


# Larry, https://www.youtube.com/watch?v=q1f7Bwr3ajM
class KthLargest:
    # O(N log K)
    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k
        
        # O(N)
        for x in nums:
            # O(log K)
            heapq.heappush(self.h, x)
            
            if len(self.h) > self.k:
                heapq.heappop(self.h)

    # O(log K)
    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        
        if len(self.h) > self.k:
            heapq.heappop(self.h)

        return self.h[0]
    
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# 04/08/2022 17:19